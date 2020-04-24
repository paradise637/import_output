from xls import Property
import xlwt
from xlutils.copy import copy
import xlrd
from type import Type

workbook = xlrd.open_workbook("io_xls/wbmb.xls")
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
education = dh.education()
professional = dh.professional()
safety =dh.safety()
typewb = ty.type_wb()
phone = dh.phone()
phone_sn = dh.phone_SN()
police = dh.police()
ph = dh.other_telephone()
name_w = ty.name_wb()
address = ty.address()

# 导入excel
worksheet.write(1,0,name_w)
worksheet.write(1,1,address)
worksheet.write(1,2,"文博单位")
worksheet.write(1,3,typewb)
worksheet.write(1,4,"展示处")
worksheet.write(1,5,safety)
worksheet.write(1,6,name)
worksheet.write(1,7,telephone)
worksheet.write(1,8,identity)
worksheet.write(1,9,phone)
worksheet.write(1,10,phone_sn)
worksheet.write(1,11,"丹东市公安局")
worksheet.write(1,12,"元宝分局")
worksheet.write(1,13,"于家派出所")
worksheet.write(1,14,police)
worksheet.write(1,15,ph)
worksheet.write(1,16,"123.40466022491456")
worksheet.write(1,17,"41.833858209692046")


# 保存文件
old_content.save('io_xls/wbmb.xls')
