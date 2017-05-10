import xlrd
import xlwt
from idlist import Reader  # this class is read ids from file and put them to list
from marker import Marker  # this class is separate id of item in cell-content
from checker import Checker  # this class is check item ids according to id list

checked = []
x = 0
y = 0

book = xlrd.open_workbook('Оборотно-сальдовая.xls', encoding_override='cp1251', formatting_info=True)  # open exel-table
sheet = book.sheet_by_index(0)

new_book = xlwt.Workbook()  # creating new exel-table for sorted data
new_book_sheet = new_book.add_sheet('breed_to_breath')

check = Reader().ids(file='param.txt')  # reading item ids from file

for i in range(7, sheet.nrows-6):  # the CORE... cycle for soring data
    cell = sheet.cell_value(i, 0)
    marker = Marker().marker(cell)
    if marker in check:
        checked.append(marker)
        k = sheet.cell_value(i+1, 5)  # quantity of item at the end of term
        p = sheet.cell_value(i, 5)  # price at the end of term
        print(marker, 'kol-vo:', k, 'Price:', p)
        new_book_sheet.write(x, y, cell)  # x-stroka, y - stolbets
        new_book_sheet.write(x, y+1, k)
        new_book_sheet.write(x, y+2, p)
        x += 1

print(Checker().checked(check, checked))
new_book.save('sort-test.xls')
