from xls import Property
import xlwt
from xlutils.copy import copy
import xlrd
from type import Type

workbook = xlrd.open_workbook("io_xls/yymb.xls")
# 对数据表格进行复制
old_content = copy(workbook)
worksheet = old_content.get_sheet(0)
# 实例化类
dh = Property()
ty = Type()


# 调用类中的方法
name = dh.name()
telephone = dh.telephone()
identity = dh.identity()
safety =dh.safety()
phone = dh.phone()
phone_sn = dh.phone_SN()
nf = dh.number_fifteen()
th = ty.type_hospital()
police = dh.police()
ph = dh.other_telephone()
name_h = ty.name_hospital()
add_h = ty.address()


# 导入excel
worksheet.write(1,0,name_h)
worksheet.write(1,1,add_h)
worksheet.write(1,2,"医院")
worksheet.write(1,3,th)
worksheet.write(1,4,"手术室")
worksheet.write(1,5,safety)
worksheet.write(1,6,name)
worksheet.write(1,7,telephone)
worksheet.write(1,8,identity)
worksheet.write(1,9,name)
worksheet.write(1,10,telephone)
worksheet.write(1,11,identity)
worksheet.write(1,12,phone)
worksheet.write(1,13,phone_sn)
worksheet.write(1,14,nf)
worksheet.write(1,15,"丹东市公安局")
worksheet.write(1,16,"元宝分局")
worksheet.write(1,17,"于家派出所")
worksheet.write(1,18,police)
worksheet.write(1,19,ph)
worksheet.write(1,20,"123.40466022491456")
worksheet.write(1,21,"41.833858209692046")



# 保存文件
old_content.save('io_xls/yymb.xls')
