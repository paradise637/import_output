from xls import Property
import xlwt
from xlutils.copy import copy
import xlrd
from type import Type

workbook = xlrd.open_workbook("io_xls/symb.xls")
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
phone = dh.phone()
phone_sn = dh.phone_SN()
nf = dh.number_fifteen()
police = dh.police()
ot = dh.other_telephone()
to = ty.type_oil()
name_s = ty.name_oil()
address = ty.address()


# 导入excel
worksheet.write(1,0,name_s)
worksheet.write(1,1,address)
worksheet.write(1,2,"散装汽油")
worksheet.write(1,3,name)
worksheet.write(1,4,telephone)
worksheet.write(1,5,identity)
worksheet.write(1,6,name)
worksheet.write(1,7,telephone)
worksheet.write(1,8,identity)
worksheet.write(1,9,phone)
worksheet.write(1,10,phone_sn)
worksheet.write(1,11,nf)
worksheet.write(1,12,"丹东市公安局")
worksheet.write(1,13,"元宝分局")
worksheet.write(1,14,"于家派出所")
worksheet.write(1,15,police)
worksheet.write(1,16,ot)
worksheet.write(1,17,"123.40466022491456")
worksheet.write(1,18,'41.833858209692046')
worksheet.write(1,19,to)



# 保存文件
old_content.save('io_xls/symb.xls')
