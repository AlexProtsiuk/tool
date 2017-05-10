import xlrd
import xlwt
from idlist import Reader  # this class is read ids from file and put them to list
from marker import Marker  # this class is separate id of item in cell-content

# source = 'Оборотно-сальдовая.xls'
# config = 'param.txt' - list of cleaning staff


class Akt201:

    def akt(self, source, config, check):
        self.source = source
        self.config = config
        self.check = check
        checked = []
        x = 0
        y = 0

        book = xlrd.open_workbook(source, encoding_override='cp1251', formatting_info=True)  # open exel-table
        sheet = book.sheet_by_index(0)

        new_book = xlwt.Workbook()  # creating new exel-table for sorted data
        new_book_sheet_wash = new_book.add_sheet('миючи')
        new_book_sheet_staff = new_book.add_sheet('хлам')

        for i in range(7, sheet.nrows-6):  # the CORE... cycle for soring data
            cell = sheet.cell_value(i, 0)
            marker = Marker().marker(cell)
            if marker in check:
                checked.append(marker)
                k = sheet.cell_value(i+1, 5)  # quantity of item at the end of term
                p = sheet.cell_value(i, 5)  # price at the end of term
                print(marker, 'kol-vo:', k, 'Price:', p)
                new_book_sheet_wash.write(x, y, cell)  # x-stroka, y - stolbets
                new_book_sheet_wash.write(x, y+1, k)
                new_book_sheet_wash.write(x, y+2, p)
                x += 1
