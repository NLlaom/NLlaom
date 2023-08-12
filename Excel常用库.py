import xlrd  # 读取excel使用的库
import xlwings as xw  # 写入excel使用的库
import os
# --------------  读操作   --------------
# filename = r"C:\\Users\\Wanna_win_the_horse\\Desktop\\场景表.xlsx"
# data = xlrd.open_workbook(filename)  # 获取excel 表格对象
# table = data.sheet_by_name('Sheet1')  # 获取excel中的工作表
# names = data.sheet_names()  # 获取excel表中工作表的名称
# rows = table.nrows  # 获取工作表中的行数 ---> 4
# row = table.row(2)  # 数据格式[text:'小唐', number:20.0, text:'业务员', number:18956478958.0]
# row2 = table.row_len(2)  # 第二行有多少列
# row3 = table.cell(2, 3)  # 2行三列单元格里面数据格式和值
# row4 = table.cell_value(2, 3)  # 2行三列单元格里面的值

# ------------------- 写操作 ------------------
# filename = r"C:\\Users\\Wanna_win_the_horse\\Desktop\\场景表.xlsx"
# filename2 = r"C:\\Users\\Wanna_win_the_horse\\Desktop\\场景表2.xlsx"

# app = xw.App(visible=True, add_book=False)
# wb = app.books.open(filename)  # 每次都会开一个Excel进程
# wb = xw.Book(filename)  # 只会开一个Excel进程
# wb.save(filename2)  # 给路经参数则是另存为 保存工作簿
# wb.close()  # 可以省略
# app.quit()  # 退出Excel

# --------------- 新建一个Excel表格 --------------
# filename = r"C:\\Users\\Wanna_win_the_horse\\Desktop\\场景表.xlsx"
# filename2 = r"C:\\Users\\Wanna_win_the_horse\\Desktop\\场景表2.xlsx"
# if os.path.exists(filename2):
#     os.remove(filename2)
#
# app = xw.App(visible=True, add_book=False)
# wb = app.books.add()
# wb.sheets['Sheet1'].range('A1').value = '小唐'
# wb.save(filename2)
# wb.close()
# app.quit()
