from xls import Property
import xlwt
from xlutils.copy import copy
import xlrd
from type import Type

workbook = xlrd.open_workbook("io_xls/gxmb.xls")
# 对数据表格进行复制
old_content = copy(workbook)
worksheet = old_content.get_sheet(0)
# 实例化类
dh = Property()
ty = Type()
# 调用类中的方法
name = dh.name()
identity = dh.identity()
birthday = dh.birthday()
documents = dh.documents()
college =dh.college()
eductional_system =dh.eductional_system()
time_school =dh.time_school()
gx = ty.name_school()
address = ty.address()
ts = ty.type_school()
safe = dh.safety()
tel = dh.telephone()
phone = dh.phone()
phone_sn = dh.phone_SN()
police = dh.police()
other_p = dh.other_telephone()


# 导入excel
worksheet.write(1,0,gx)
worksheet.write(1,1,address)
worksheet.write(1,2,"高校")
worksheet.write(1,3,ts)
worksheet.write(1,4,"教学楼")
worksheet.write(1,5,safe)
worksheet.write(1,6,name)
worksheet.write(1,7,tel)
worksheet.write(1,8,identity)
worksheet.write(1,9,name)
worksheet.write(1,10,tel)
worksheet.write(1,11,identity)
worksheet.write(1,12,phone)
worksheet.write(1,13,phone_sn)
worksheet.write(1,14,"丹东市公安局")
worksheet.write(1,15,"元宝分局")
worksheet.write(1,16,"于家派出所")
worksheet.write(1,17,police)
worksheet.write(1,18,other_p)
worksheet.write(1,19,"123.40466022491456")
worksheet.write(1,20,"41.833858209692046")






# 保存文件
old_content.save('io_xls/gxmb.xls')
