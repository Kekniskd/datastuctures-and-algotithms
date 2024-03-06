a = ['W Denis Custodian', 'W Denis Custodian', '12%', '6834231', 'Sabria T', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 37.0, 4847.0, 13100.0, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Carrier-AXA Risk-EPL Cover-EPL | Amended BDX September 2023.xlsx']
b = ['W Denis Custodian', 'W Denis Custodian', '12%', '6834231', 'Sabria T', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 37.0, 5352.05, 14465.0, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Carrier-AXA Risk-DO Cover-DO | Amended BDX September 2023.xlsx']
result = []

for val_a, val_b in zip(a, b):
    if isinstance(val_a, (int, float)) and isinstance(val_b, (int, float)):
        result.append(val_a + val_b)
    else:
        result.append(val_a if val_a else val_b)

print(result)

