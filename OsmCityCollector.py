import openpyxl
import csv

# Load Excel file
workbook = openpyxl.load_workbook('staedte.xlsx')
sheet = workbook['Städte']

# Open CSV file for writing
with open('names.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    # Extract data from Excel and write to CSV
    for row in sheet.iter_rows(min_row=8, min_col=7, values_only=True):  # Assuming names start from G8
        if row[0]:
            name = row[0].split(',')[0]  # Split by semicolon and take the first part
            writer.writerow({'name': name.strip()})  # Remove leading/trailing spaces

print("CSV file 'names.csv' has been created with names extracted from Excel.")
