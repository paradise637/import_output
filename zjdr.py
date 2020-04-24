from xls import Property
import xlwt
from xlutils.copy import copy
import xlrd

workbook = xlwt.Workbook(encoding = 'ascii')
workbook = xlwt.Workbook(encoding = 'utf-8')
workbook = xlrd.open_workbook("zjdr.xls")
# 对数据表格进行复制
old_content = copy(workbook)
worksheet = old_content.get_sheet(0)
# 实例化类
dh = Property()
# 调用类中的方法
telephone = dh.telephone()
identity = dh.identity()
passway = dh.passway()
io = dh.io()
ns = dh.number_seven()
time = dh.local_time()

# 导入excel
worksheet.write(1,0,"")
worksheet.write(1,1,passway)
worksheet.write(1,2,telephone)
worksheet.write(1,3,identity)
worksheet.write(1,4,io)
worksheet.write(1,5,ns)
worksheet.write(1,6,"丹东理工大学")
worksheet.write(1,7,time)
worksheet.write(1,8,"丹东市公安局")
worksheet.write(1,9,"元宝分局")
worksheet.write(1,10,"于家派出所")


# 保存文件
old_content.save('zjdr.xls')
