from xls import Property
import xlwt
from xlutils.copy import copy
import xlrd

workbook = xlwt.Workbook(encoding = 'ascii')
workbook = xlwt.Workbook(encoding = 'utf-8')
workbook = xlrd.open_workbook("io_xls/gxlxsdr.xls")

# 对数据表格进行复制
old_content = copy(workbook)
worksheet = old_content.get_sheet(0)

# 实例化类
dh = Property()

# 调用类中的方法
name = dh.name()
identity = dh.identity()
birthday = dh.birthday()
documents = dh.documents()
sex = dh.sex()
college = dh.college()
eductional_system =dh.eductional_system()
time_school =dh.time_school()
ranges =dh.ranges()


# 导入excel
worksheet.write(1,0,name)
worksheet.write(1,1,documents)
worksheet.write(1,2,identity)
worksheet.write(1,3,sex)
worksheet.write(1,4,birthday)
worksheet.write(1,5,"丹东医科大学")
worksheet.write(1,6,college)
worksheet.write(1,7,"MBBS")
worksheet.write(1,8,eductional_system)
worksheet.write(1,9,time_school)
worksheet.write(1,10,"丹东市公安局")
worksheet.write(1,11,"元宝分局")
worksheet.write(1,12,"于家派出所")



# 保存文件
old_content.save('gxlxsdr.xls')
