import xlrd, csv, os


os.chdir('ex1_data_conversion')

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


# Process the fields
def parse_places_data(sheet):
    for row in sheet:
        row['code'] = int(row['code'])
        row['level'] = int(row['level'])
        row['lat'] = parse_field_latlng(row['latlng'])['lat']
        row['lon'] = parse_field_latlng(row['latlng'])['lon']
        del row['latlng']
        try:
            row['population'] = int(row['population'])
        except ValueError:
            print('No population data')


sheet = read_xls_sheet(xlrd_sheet)
parse_places_data(sheet)


def print_sheet(dat):
     for row in sheet:
         print(row)

print_sheet(sheet)

print(str(sheet[1].keys))

for key in sheet[1].keys():
    print(key)


# write rows to the new file

names = ['code', 'name', 'population', 'area', 'type', 'level', 'lat', 'lon']

output = open('dict.csv', 'w', newline='')
writer = csv.DictWriter(output, fieldnames = names)
writer.writeheader()
writer.writerows(sheet)


#
#
# # close the file again
# outfile.close()
