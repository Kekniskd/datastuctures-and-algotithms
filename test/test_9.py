import logging
import re
from datetime import datetime


def extract_month_and_year_format_1(filename):
    # Regular expression pattern to match month and year in the format MM.YY
    pattern = r'\b(\d{2})\.(\d{2})\b'

    # Search for the pattern in the filename
    match = re.search(pattern, filename)

    if match:
        # Extract the month and year parts
        month = match.group(1)
        year = match.group(2)
        return month, year
    else:
        return None, None


def extract_month_and_year(path, only_month=False):
    month = None
    year = None
    input_string = path.split('/')[-1]
    pattern = re.compile(r'-\s*(2[1-9])\b')
    input_string = re.sub(pattern, r'20\1', input_string)
    input_string = input_string.replace('.xlsx', '').replace('.xls', '').replace('.ibmsg', '').replace('(', '').replace(
        ')', '')
    words = input_string.split()
    pattern = r'\b(\d{2})\s*(\d{4})\b'
    match = re.search(pattern, input_string)

    # replacing Sept with sep
    input_string = re.sub(r'\bsept\b', 'Sep', input_string, flags=re.IGNORECASE)
    words = input_string.split()
    pattern = r'\b(\d{2}).?\s*(\d{4})\b'
    match = re.search(pattern, input_string)

    # need to add a check here for invalid String going through the same regex example 6767576 - this particular string will pass as Date.
    if match:
        if int(match.group(1)) <= 31 and 2016 <= int(match.group(2)) <= 2030:
            return int(match.group(1)), int(match.group(2))
    for i, word in enumerate(words):
        # Search for the pattern in the filename
        try:
            match = re.search(r'\b(\d{2})\.(\d{2})\b', word)

            if match:
                # Extract the month and year parts
                month = int(match.group(1))
                year = int(match.group(2))
        except Exception as e:
            pass
            # logging.info(e)

        try:
            match = re.match(r'(\d{4})(\d{2})(\d{2})', word)
            if match:
                year, month, day = match.groups()
                year = int(year)
                month = int(month)
        except Exception as e:
            pass
            # logging.info(e)

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

    # extract_month_and_year_format_1()
    # Get current month and year if not extracted
    month_present = True
    if not month:
        current_date = datetime.now()
        month = current_date.month
        month_present = False
    if not year:
        current_date = datetime.now()
        year = current_date.year
        current_month = current_date.month
        if month > current_month:
            year = year - 1
    if only_month:
        return month, month_present
    return month, year


path_ = "test 20.xlsx"
print(extract_month_and_year(path_, only_month=False))
