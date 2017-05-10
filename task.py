import xlwt


new_book = xlwt.Workbook()  # creating new exel-table for sorted data
new_book_sheet = new_book.add_sheet('hell_yeah')

new_book_sheet.write(1, 3, 'Затверджую:')

new_book.save('sort-test.xls')
print('fucking done')
