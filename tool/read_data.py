import xlrd


class ReadData(object):

    def __init__(self, file):
        self.file = "./data/" + file

    def read_data(self, sheetname):
        book = xlrd.open_workbook(self.file)
        sheet = book.sheet_by_name(sheetname)
        array = []
        for i in range (1, sheet.nrows):
            array.append(sheet.row_values(i))
        return array

if __name__ == "__main__":
    # book = xlrd.open_workbook('../data/login/login.xlsx')
    # sheet = book.sheet_by_name("login_fail")
    # print(sheet.nrows)
    # array = []
    # for i in range (1, sheet.nrows):
    #     array.append(sheet.row_values(i))
    # print(array)
    datas = ReadData('../data/login/login.xlsx').read_data("login_success")
    # print(datas)
    arrays = []
    for i in range(len(datas)):
        print(tuple(datas[i]))
        # arrays.append((datas[i][1], datas[i][2], datas[i][3], datas[i][4]))
    # print(arrays)