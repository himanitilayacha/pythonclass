import xlrd
import xlwt
book=xlwt.Workbook()
sheet=book.add_sheet("sheet1")
for row in range(3):
    for col in range(4):
       sheet.write(row,col,raw_input("Entrer data : "))
book.save("second.xls")
