import xlrd

filepath=r"C:\Users\hanshik\Downloads\challenge.xlsx"

workbook=xlrd.open_workbook(filepath)
sheet=workbook.sheet_by_name("Data")


#print each row and column data

rowcount=sheet.nrows
colscount=sheet.ncols

for r in range(1,rowcount):

    for c in range(0,colscount):
        cellValue=sheet.cell_value(r,c)
        print(cellValue)

    print("*****************************************************************")
