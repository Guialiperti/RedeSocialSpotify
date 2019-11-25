import xlwt
from xlwt import Workbook

wb = Workbook()

sheet1 = wb.add_sheet('1')

lista = []

for i in range(99):
    sheet1.write(i,1,lista[i])


wb.save('ex.xls')
