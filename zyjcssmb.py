from xls import Property
import xlwt
from xlutils.copy import copy
import xlrd
from type import Type

workbook = xlrd.open_workbook("io_xls/zyjcssmb.xls")
# 对数据表格进行复制
old_content = copy(workbook)
worksheet = old_content.get_sheet(0)
# 实例化类
dh = Property()
ty = Type()
# 调用类中的方法
name = dh.name()
nation = dh.nation()
telephone = dh.telephone()
create_job_time = dh.local_time()
base = dh.base()
grade = dh.grade()
size = dh.size()
local = dh.local()
name_z = ty.name_company()

# 导入excel
worksheet.write(1,0,name_z)
worksheet.write(1,1,"基础的设施")
worksheet.write(1,2,grade)
worksheet.write(1,3,base)
worksheet.write(1,4,size)
worksheet.write(1,5,local)
worksheet.write(1,6,"02:00 - 04:00")
worksheet.write(1,7,"正常")
worksheet.write(1,8,create_job_time)
worksheet.write(1,9,create_job_time)
worksheet.write(1,10,name)
worksheet.write(1,11,telephone)
worksheet.write(1,12,"丹东市公安局")
worksheet.write(1,13,"元宝分局")
worksheet.write(1,14,"于家派出所")


# 保存文件
old_content.save('io_xls/zyjcssmb.xls')
