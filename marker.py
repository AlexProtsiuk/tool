# this class is separate id of item in cell-content


class Marker:

    def marker(self, cell):  # this method separate item-id in cell
        self.cell = cell
        new_cell = cell.strip(' ')
        marker = ''
        a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        for i in range(len(new_cell)):
            if new_cell[i] in a:
                marker += new_cell[i]
            else:
                break
        return marker

    def item(self, cell, marker):  # this method separate item-name in cell
        self.marker = marker
        self.cell = cell

        new_cell = cell.strip(' ')
        item = new_cell.strip(marker)
        return item


