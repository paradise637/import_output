from xls import Property
import xlwt
from xlutils.copy import copy
import xlrd
from type import  Type


workbook = xlrd.open_workbook("io_xls/bwrymb.xls")
# 对数据表格进行复制
old_content = copy(workbook)
worksheet = old_content.get_sheet(0)

# 实例化类
dh = Property()
ty = Type()

# 调用类中的方法
name = dh.name()
sex = dh.sex()
nation = dh.nation()
telephone = dh.telephone()
identity = dh.identity()
birthday = dh.birthday()
education = dh.education()
professional = dh.professional()
lt = dh.local_time()
address = ty.address()
address_now = dh.address_now()
name_b = ty.name_company()

# 导入excel
worksheet.write(1,0,name)
worksheet.write(1,1,sex)
worksheet.write(1,2,nation)
worksheet.write(1,3,telephone)
worksheet.write(1,4,identity)
worksheet.write(1,5,birthday)
worksheet.write(1,6,address)
worksheet.write(1,7,address_now)
worksheet.write(1,8,name_b)
worksheet.write(1,9,"罗迪士保安公司")
worksheet.write(1,10,education)
worksheet.write(1,11,professional)
worksheet.write(1,12,lt)
worksheet.write(1,13,"丹东市公安局")
worksheet.write(1,14,"元宝分局")
worksheet.write(1,15,"于家派出所")

# 保存文件
old_content.save('io_xls/bwrymb.xls')

