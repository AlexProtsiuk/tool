# this class is read ids from file and put them to list


class Reader:

    def ids(self, file):
        self.file = file
        check = []
        param = open(file, 'r')
        for line in param.readlines():
            line = line.strip('\n')
            check.append(line)
            if check[0] == 'akt':  # preparing check-list for Akt201 class
                check.remove('akt')
            else:  # preparing check-list for ostatki
                pass
        return check
