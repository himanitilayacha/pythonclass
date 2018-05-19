import xlrd

exBook = xlrd.open_workbook("name.xlsx") # name.xls , 

sheet = exBook.sheet_by_index(0)



for row in range(4):
    for col in range(3):
        cell_value = sheet.cell(row,col).value
        print cell_value,
    print ""
    
for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        cell_value = sheet.cell(row,col).value
        print cell_value,
    print ""
