import xlrd

class ReadExcel():
    def __init__(self, excelPath, sheetName="train"):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum-1):
                # 从第一行取对应values值
                values = self.table.row_values(j)
                r.append(values)
                j += 1
        return r

if __name__ == "__main__":
    filepath = "C://Users//86176//Desktop//inputData.xlsx"
    data = ReadExcel(filepath)
    print(data.dict_data())

