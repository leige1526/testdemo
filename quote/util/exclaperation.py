import xlrd


class ExcelOperation:
    def __init__(self,path=None,sheet_name=None):
        if path == None:
            path = 'C:\\Users\\admin\\Desktop\\logincase.xlsx'
        else:
            path = path
        if sheet_name == None:
            sheet_name  = '用例参数'
        else:
            sheet_name = sheet_name
        #获取工作簿
        self.workbook = xlrd.open_workbook(path)
        # 获取sheet页面
        self.sheet = self.workbook.sheet_by_name(sheet_name)

    def get_row(self):
        return self.sheet.nrows

    def get_col(self):
        return self.sheet.ncols

    def get_cell_value(self,nrow,ncol):
        if self.sheet.cell(nrow,ncol).ctype == 2:
            cell = str(self.sheet.cell_value(nrow,ncol))
        else:
            cell = self.sheet.cell_value(nrow,ncol)
        return cell

exl = ExcelOperation('C:\\Users\\admin\\Desktop\\logincase.xlsx','用例参数')
print(exl.get_cell_value(1,1))