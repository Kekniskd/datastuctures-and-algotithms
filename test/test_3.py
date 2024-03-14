COLUMNA_WITH_INDEX = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13,
    'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25,
    'AA': 26, 'AB': 27, 'AC': 28, 'AD': 29, 'AE': 30, 'AF': 31, 'AG': 32, 'AH': 33, 'AI': 34,
    'AJ': 35, 'AK': 36, 'AL': 37, 'AM': 38, 'AN': 39, 'AO': 40, 'AP': 41, 'AQ': 42,
    'AR': 43, 'AS': 44, 'AT': 45, 'AU': 46, 'AV': 47, 'AW': 48, 'AX': 49, 'AY': 50, 'AZ': 51, 'BA': 52, 'BB': 53,
    'BC': 54, 'BD': 55, 'BE': 56, 'BF': 57, 'BG': 58, 'BH': 59, 'BI': 60, 'BJ': 61, 'BK': 62,
    'BL': 63, 'BM': 64, 'BN': 65, 'BO': 66, 'BP': 67, 'BQ': 68, 'BR': 69, 'BS': 70, 'BT': 71, 'BU': 72, 'BV': 73,
    'BW': 74, 'BX': 75, 'BY': 76, 'BZ': 77, 'CA': 78, 'CB': 79, 'CC': 80, 'CD': 81
}

VALUE_DICT = {'0.12': [], '0': [], '0.12_A': [], '0.12_B': [], '0.12_C': [], '0.12_D': [], '0_A': [], '0_B': [],
              '0_C': [], '0_D': [], '0.12_commercial': [], '0.12_residential': [], '0_commercial': [],
              '0_residential': []}

PROPERTY_TYPES = ['residential', 'commercial']

ZONES = ['A', 'B', 'C', 'D']

PERCENTAGE_COLUMNS = ["Q", "T", "W", "Z", "AC", "AF", "AI", "AL", "AO", "AR", "AU", "AX", "BA", "BD", "BG", "BK", "BO",
                      "BS", "BW", "CA"]


def formula_update(rows):
    for row in rows:
        for percentage in PERCENTAGE_COLUMNS:
            idx = COLUMNA_WITH_INDEX[percentage]
            if isinstance(row[idx + 1], float):
                comm_pct = (row[idx + 1] / row[idx + 2]) * 100
                row[idx] = comm_pct
    return rows


a = [
    ['W Denis Custodian', 'W Denis Custodian', '12%', '6834231', 'Sabria T', '', '', '', '', '', '', '', '', '', '', '',
     '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 36.53750651116772, 52671.07000000001,
     144156.16999999998, 148.00023648833022, 6508.88, 17591.55, '', '', '', '', '', '', '', '', '', '', '', '', '', '',
     '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
     'Carrier-AXA Risk-EPL Cover-EPL | BDX May w_denis.xlsx'],
    ['W Denis Custodian', 'W Denis Custodian', '0%', '6834231', 'Sabria T', '', '', '', '', '', '', '', '', '', '', '',
     '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
     '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
     '', '', '', '', '', '', '', 'Carrier-AXA Risk-EPL Cover-EPL | BDX May w_denis.xlsx'],
    ['W Denis Custodian Office', 'W Denis Custodian Office', '12%', '6930677', 'Sabria T', '', '', '', '', '', '', '',
     '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 37.0, 125.06, 338.0, 37.0, 319.68, 864.0, '', '',
     '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
     '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
     'Carrier-AXA Risk-LIA Cover-PL | BDX May w_denis.xlsx'],
    ['W Denis Custodian Office', 'W Denis Custodian Office', '0%', '6930677', 'Sabria T', '', '', '', '', '', '', '',
     '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
     '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
     '', '', '', '', '', '', '', '', '', '', '', 'Carrier-AXA Risk-LIA Cover-PL | BDX May w_denis.xlsx']]

rows = formula_update(a)
for i in rows:
    print(i)
