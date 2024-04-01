import re
from datetime import datetime


def extract_month_and_year(input_string, only_month=False):
    month = None
    year = None
    pattern = re.compile(r'-\s*(2[1-9])\b')
    input_string = re.sub(pattern, r'20\1', input_string)
    input_string = input_string.replace('.xlsx', '').replace('.xls', '').replace('.ibmsg', '').replace('(', '').replace(
        ')', '')

    # replacing Sept with sep
    input_string = re.sub(r'\bsept\b', 'Sep', input_string, flags=re.IGNORECASE)
    words = input_string.split()
    pattern = r'\b(\d{2}).?\s*(\d{4})\b'
    match = re.search(pattern, input_string)

    # need to add a check here for invalid String going through the same regex example 6767576 - this particular string will pass as Date.
    if match:
        # if int(match.group(1)) <= 31 and int(match.group(2)) >= 2016 and int(match.group(2)) <= 2030:
        if int(match.group(1)) <= 31 and 2016 <= int(match.group(2)) <= 2030:
            return int(match.group(1)), int(match.group(2))
    for i, word in enumerate(words):
        if re.match(r'\d{4}', word):
            word = re.sub(r'[^0-9]', '', word)
            year = int(word)
        else:
            try:
                date = datetime.strptime(word, '%B')
                month = date.month
            except ValueError:
                try:
                    date = datetime.strptime(word, '%b')
                    month = date.month
                except ValueError:
                    pass
        if year and (int(year) < 2016 or int(year) > 2030):
            year = None
        if month and year:
            break

        # Check previous word for month if year is found first
        if year and i > 0:
            previous_word = words[i - 1]
            try:
                date = datetime.strptime(previous_word, '%B')
                month = date.month
            except ValueError:
                try:
                    date = datetime.strptime(previous_word, '%b')
                    month = date.month
                except ValueError:
                    pass
        if year and (int(year) < 2016 or int(year) > 2030):
            year = None
        if month and year:
            break

    # Get current month and year if not extracted
    month_present = True
    if only_month:
        return month, month_present
    return month, year


test1 = extract_month_and_year('BDX_Tradesman_Financial_PolicyBee_24 November 2023.xlsx')
test2 = extract_month_and_year('BDX_Tradesman_Financial_PolicyBee_Monthly_23.xlsx')
print(f'test1: {test1}')
print(f'test2: {test2}')


