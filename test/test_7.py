import re
import pandas as pd
from datetime import datetime

month_dict = {
    'jan': 'january',
    'feb': 'february',
    'mar': 'march',
    'apr': 'april',
    'jun': 'june',
    'jul': 'july',
    'aug': 'august',
    'sep': 'september',
    'oct': 'october',
    'nov': 'november',
    'dec': 'december'
}


def extract_month_from_excel(file_path, start_row, end_row):
    wb = pd.read_excel(file_path, header=None)

    month = None
    month_num = None
    month_cell = None
    for index, row in wb.iterrows():
        for col_index, cell_value in enumerate(row):
            if str(cell_value).lower() == 'month':
                month_cell = (index, col_index)
                break
        if month_cell:
            break

    if month_cell is None:
        return "Month cell not found."

    extracted_months = []

    start_row_index = max(0, month_cell[0] - 1)
    end_row_index = min(len(wb), month_cell[0] + 2)
    start_col_index = max(0, month_cell[1] - 1)
    end_col_index = min(len(wb.columns), month_cell[1] + 2)

    for row_index in range(start_row_index, end_row_index):
        for col_index in range(start_col_index, end_col_index):
            cell_value = wb.iloc[row_index, col_index]
            month_match = re.search(
                r'(january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|jun|jul|aug|sep|oct|nov|dec)',
                str(cell_value).lower())
            if month_match:
                month = month_match.group(0)

    if not month:
        for row in wb.loc[start_row:end_row].iterrows():
            for cell_value in row:
                month_match = re.search(
                    r'(january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|jun|jul|aug|sep|oct|nov|dec)',
                    str(cell_value).lower())
                if month_match:
                    extracted_months.append(month_match.group(0))

    if month:
        month_num = datetime.strptime(month,
                                      "%B").month if month not in month_dict.keys() else datetime.strptime(
            month_dict[month], "%B").month

    elif extracted_months:
        month_num = datetime.strptime(month,
                                      "%B").month if extracted_months[-1] not in month_dict.keys() else datetime.strptime(
            month_dict[extracted_months[-1]], "%B").month
    return month_num


excel_file_path = 'test.xlsx'
months = extract_month_from_excel(excel_file_path, 0, 4)
print(months)
