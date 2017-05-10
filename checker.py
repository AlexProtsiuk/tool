# this class is check item ids according to id list


class Checker:

    def checked(self, check, checked):
        self.check = check
        self.checked = checked
        f = []
        if len(check) == len(checked):
            print('all items are checked')
        else:
            for i in range(0, len(check)):
                if check[i] in checked:
                    pass
                else:
                    f.append(check[i])
        print('items not founded:', f)
