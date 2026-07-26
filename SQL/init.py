"""Rebuild the local SQLite practice DB and run .sql files against it.

No installs needed -- Python's stdlib sqlite3 bundles the engine.

    python SQL/init.py                     rebuild auction.db from schema/
    python SQL/init.py query.sql           rebuild, then run query.sql
    python SQL/init.py -k query.sql        keep the current db, just run the file
    python SQL/init.py -i                  rebuild, then drop into a REPL
"""

import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).parent
DB = ROOT / "auction.db"


def split_statements(sql):
    """Split a script into statements, respecting string literals and comments."""
    statements, buf = [], ""
    for line in sql.splitlines(keepends=True):
        buf += line
        if sqlite3.complete_statement(buf):
            statements.append(buf.strip())
            buf = ""
    if buf.strip():
        statements.append(buf.strip())
    return statements


def print_table(cur):
    if cur.description is None:
        return
    headers = [d[0] for d in cur.description]
    rows = [["NULL" if v is None else str(v) for v in row] for row in cur.fetchall()]
    widths = [
        max([len(h)] + [len(r[i]) for r in rows])
        for i, h in enumerate(headers)
    ]
    line = "-+-".join("-" * w for w in widths)
    print(" | ".join(h.ljust(w) for h, w in zip(headers, widths)))
    print(line)
    for r in rows:
        print(" | ".join(c.ljust(w) for c, w in zip(r, widths)))
    print(f"({len(rows)} row{'s' if len(rows) != 1 else ''})\n")


def rebuild(conn):
    for path in sorted((ROOT / "schema").glob("*.sql")):
        conn.executescript(path.read_text(encoding="utf-8"))
        print(f"loaded {path.relative_to(ROOT)}")
    conn.commit()


def run_file(conn, path):
    for stmt in split_statements(Path(path).read_text(encoding="utf-8")):
        if not stmt.strip(" ;\n"):
            continue
        cur = conn.execute(stmt)
        print_table(cur)
    conn.commit()


def repl(conn):
    print("sqlite REPL -- end statements with ';', blank line or Ctrl-C to quit")
    buf = ""
    while True:
        try:
            line = input("... " if buf else "sql> ")
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if not line.strip() and not buf:
            return
        buf += line + "\n"
        if sqlite3.complete_statement(buf):
            try:
                print_table(conn.execute(buf))
            except sqlite3.Error as exc:
                print(f"error: {exc}\n")
            buf = ""


def main():
    args = sys.argv[1:]
    keep = "-k" in args
    interactive = "-i" in args
    files = [a for a in args if not a.startswith("-")]

    conn = sqlite3.connect(DB)
    conn.execute("PRAGMA foreign_keys = ON")

    if not keep:
        rebuild(conn)

    for f in files:
        print(f"\n-- {f}")
        run_file(conn, f)

    if interactive:
        repl(conn)

    conn.close()


if __name__ == "__main__":
    main()
