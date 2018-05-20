
import xlrd


exBook=xlrd.open_workbook("himani1.xlsx")


sheet=exBook.sheet_by_index(0)
t_rows=sheet.nrows
t_cols=sheet.ncols


for i in range(t_rows):
    for j in range(t_cols):
        cell_value=sheet.cell(i,j).value
        print cell_value,
    print ""

