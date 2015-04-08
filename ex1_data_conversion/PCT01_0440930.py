# python 3

__author__      = "Stefan Fleck"

import xlrd, csv


# open file
xlrd_sheet = xlrd.open_workbook('assignment01.xlsx')
xlrd_sheet = xlrd_sheet.sheets()[0]


# I want to be able to refer to rows by key rather than by index so i'll use a
# list of dictionaries instead of a list of lists as in the lecture.
# Filtering by county also happens in this step
def read_xls_sheet(sheet, county_filter=3):
    keys = [sheet.cell(0, col_index).value for col_index in range(0, sheet.ncols)]
    data = []

    for row_index in range(1, sheet.nrows):
        row = {keys[col_index]: sheet.cell(row_index, col_index).value
            for col_index in range(0, sheet.ncols)}

        if str(row['code'])[0] == str(county_filter):
            print('row ' + str(int(row['code'])) + ' appended')
            data.append(row)
        else:
            print('row ' + str(int(row['code'])) + ' skipped')

    return(data)


def parse_field_latlng(x):
    x = x.replace('lat:', '')
    x = x.replace('lon:', '')
    x = x.replace('E', '')
    x = x.replace('N', '')
    x = x.replace(';', ' ')
    x = x.split()

    res = {}
    res['lat'] = float(x[0])
    res['lon'] = float(x[1])

    return res


def parse_places_data(sheet):
    for row in sheet:
        # Recode and split latlang field
        row['code'] = int(row['code'])
        row['level'] = int(row['level'])
        row['lat'] = parse_field_latlng(row['latlng'])['lat']
        row['lon'] = parse_field_latlng(row['latlng'])['lon']
        del row['latlng']

        try:
            row['population'] = int(row['population'])
        except ValueError:
            pass


# Ececute function
sheet = read_xls_sheet(xlrd_sheet)
parse_places_data(sheet)


## Output to csv
fields = ['code', 'name', 'population', 'area', 'type', 'level', 'lat', 'lon']
with open('dict.csv', 'w', newline='') as output:
    writer = csv.DictWriter(output, fieldnames = fields)
    writer.writeheader()
    writer.writerows(sheet)
