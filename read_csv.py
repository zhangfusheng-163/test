import xlrd
# import pandas as pd


def read_teach_excel(path):
    wb=xlrd.open_workbook(path)
    sheet1=wb.sheet_by_index(0)
    nrow=sheet1.nrows
    ncol=sheet1.ncols
    teach_name=[]
    teach_numb=[]
    teach_id=[]
    for i in range(nrow):
        teach_name.append(sheet1.cell_value(i,0))
        teach_numb.append(sheet1.cell_value(i,1))
        teach_id.append(sheet1.cell_value(i,2))
    print(teach_id)


def read_inform_excel(path):
    wb=xlrd.open_workbook(path)
    sheet1=wb.sheet_by_index(0)
    nrow=sheet1.nrows
    ncol=sheet1.ncols
    teach_name=[]
    teach_numb=[]
    teach_id=[]
    for i in range(nrow):
        teach_name.append(sheet1.cell_value(i,0))
        teach_numb.append(sheet1.cell_value(i,1))
        teach_id.append(sheet1.cell_value(i,2))
    print(teach_id)

# def


if __name__=='__main__':
    teach_path = '/home/xunlong/code/csv/teacher_Data.xlsx'
    inform_pth = '/home/xunlong/code/csv/all_inform.xlsx'
    # read_excel(teach_path)

# tp = xlrd.open_workbook(teach_path)
# ip=xlrd.open_workbook(inform_pth)

