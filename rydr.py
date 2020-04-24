from xls import Property
import xlwt
from xlutils.copy import copy
import xlrd
from type import  Type

workbook = xlrd.open_workbook("io_xls/rydr.xls")
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
identity = dh.identity()
birthday = dh.birthday()
professional = dh.professional()
sex = dh.sex()
lt = dh.local_time()
documents = dh.documents()
dp = dh.department()
address = ty.address()
name_t =ty.name_wb()


# 导入excel
worksheet.write(1,0,name)
worksheet.write(1,1,sex)
worksheet.write(1,2,nation)
worksheet.write(1,3,telephone)
worksheet.write(1,4,birthday)
worksheet.write(1,5,lt)
worksheet.write(1,6,"中国")
worksheet.write(1,7,documents)
worksheet.write(1,8,identity)
worksheet.write(1,9,address)
worksheet.write(1,10,address)
worksheet.write(1,11,name_t)
worksheet.write(1,12,professional)
worksheet.write(1,13,dp)
worksheet.write(1,14,"丹东市公安局")
worksheet.write(1,15,"元宝分局")
worksheet.write(1,16,"于家派出所")


# 保存文件
old_content.save('io_xls/rydr.xls')
