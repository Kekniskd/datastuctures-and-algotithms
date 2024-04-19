import re
import pandas as pd


def extract_month_from_excel(file_path, start_row, end_row):
    # Load the Excel workbook
    # wb = openpyxl.load_workbook(file_path)
    wb = pd.read_excel(file_path)
    print(wb.head())
    # Select the active sheet

    # Initialize a list to store extracted months
    extracted_months = []

    # Iterate through specified rows in the sheet
    for row in wb.loc[start_row:end_row].iterrows():
        print(row)
        for cell_value in row:
            # Apply regex to extract month
            month_match = re.search(
                r'(January|February|March|April|May|June|July|August|September|October|November|December)', str(cell_value))
            if month_match:
                extracted_months.append(month_match.group(0))

    return extracted_months


# Example usage
excel_file_path = 'BDX_Tradesman_Financial_PolicyBee_Monthly_23.xlsx'  # Replace with your Excel file path
months = extract_month_from_excel(excel_file_path, 0, 4)
if months is not None:
    print(months)
