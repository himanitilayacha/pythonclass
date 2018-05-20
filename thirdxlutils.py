import xlrd,xlwt
book=xlwt.Workbook()
sheet=book.add_sheet("sheet1")
for row in range(2):
    for col in range(4):
       sheet.write(row,col,raw_input("Entrer data : "))
book.save("second.xls")

from xlutils.copy import copy
read_book=xlrd.open_workbook("second.xls")
update_book=copy(read_book)
sheet=update_book.get_sheet(0)

