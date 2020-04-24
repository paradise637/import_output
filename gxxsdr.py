from xls import Property
import xlwt
from xlutils.copy import copy
import xlrd

workbook = xlwt.Workbook(encoding = 'ascii')
workbook = xlwt.Workbook(encoding = 'utf-8')
workbook = xlrd.open_workbook("io_xls/gxxsdr.xls")
# 对数据表格进行复制
old_content = copy(workbook)
worksheet = old_content.get_sheet(0)
# 实例化类
dh = Property()

# 调用类中的方法
name = dh.name()
nation = dh.nation()
telephone = dh.telephone()
identity = dh.identity()
identity_code =dh.identity_code()
documents =dh.documents()
nation_code =dh.nation_code()
sex = dh.sex()
time_school = dh.time_school()
sex_code = dh.sex_code()
ranges = dh.ranges()

# 导入excel
worksheet.write(1,0,name)
worksheet.write(1,1,identity_code)
worksheet.write(1,2,documents)
worksheet.write(1,3,identity)
worksheet.write(1,4,nation_code)
worksheet.write(1,5,nation)
worksheet.write(1,6,sex_code)
worksheet.write(1,7,sex)
worksheet.write(1,8,'江西赣州')
worksheet.write(1,9,telephone)
worksheet.write(1,10,"丹东理工学院")
worksheet.write(1,11,"")
worksheet.write(1,12,time_school)
worksheet.write(1,13,"丹东市公安局")
worksheet.write(1,14,"元宝分局")
worksheet.write(1,15,"于家派出所")


# 保存文件
old_content.save('gxxsdr.xls')
