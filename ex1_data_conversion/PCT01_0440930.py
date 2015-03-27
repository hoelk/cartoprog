import xlrd
import csv

import sys
print(sys.version)

# open file
xlrd_sheet = xlrd.open_workbook('assignment01.xlsx')
xlrd_sheet = xlrd_sheet.sheets()[0]

# read header values into the list


# Read in rows, store in data structure. I want to be able to refer to rows
# by key rather than by index so i'll use a list of dictionaries
def read_xls_sheet(sheet):
    keys = [sheet.cell(0, col_index).value for col_index in range(0, sheet.ncols)]
    data = []

    for row_index in range(1, sheet.nrows):
        print("Processing row" + str(row_index) + "...")
        cell = {keys[col_index]: sheet.cell(row_index, col_index).value
            for col_index in range(0, sheet.ncols)}
        data.append(cell)

    return(data)

# Process the fields
def parse_places_data(sheet):
    for row in sheet:
        row['code'] = int(row['code'])
        try:
            row['population'] = int(row['population'])
        except ValueError:
            print('No population data')


sheet = read_xls_sheet(xlrd_sheet)
parse_places_data(sheet)

            #
        #     # # convert numbers
        #     # if row > 0:
        #     #     row_data[0] = int(row_data[0])
        #     #     row_data[1] = unicode(row_data[1]).encode('utf8')
        #     #     row_data[7] = int(row_data[7])
        #     #
        #     #     # Dealt with empty strings
        #     #     try:
        #     #         row_data[4] = int(row_data[4])
        #     #     except ValueError:
        #     #         pass # do nothing
        #
        #     # if row == 0 or str(row_data[0])[0] == '2':  # string is like list so that accesses first letter!


def print_sheet(dat):
     for i in sheet:
         print(i)

print_sheet(sheet)
