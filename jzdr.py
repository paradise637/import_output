from xls import Property
import xlwt
from xlutils.copy import copy
import xlrd

workbook = xlwt.Workbook(encoding = 'ascii')
workbook = xlwt.Workbook(encoding = 'utf-8')
workbook = xlrd.open_workbook("io_xls/jzdr.xls")
# 对数据表格进行复制
old_content = copy(workbook)
worksheet = old_content.get_sheet(0)
# 实例化类
dh = Property()
# 调用类中的方法
name = dh.name()
sex = dh.sex()
equipment_number = dh.equipment_number()
identity = dh.identity()
number_three =dh.number_three()
other_name = dh.other_name()
tm = dh.type_medicine()
tel =dh.telephone()
time = dh.local_time()
ranges = dh.ranges()

# 导入excel
worksheet.write(1,0,name)
worksheet.write(1,1,sex)
worksheet.write(1,2,equipment_number)
worksheet.write(1,3,tel)
worksheet.write(1,4,identity)
worksheet.write(1,5, number_three)
worksheet.write(1,6,name)
worksheet.write(1,7,'呼吸道感染')
worksheet.write(1,8,"头孢呋辛酯片（赛）")
worksheet.write(1,9,tm)
worksheet.write(1,10,"丹东市中心医院")
worksheet.write(1,11,time)
worksheet.write(1,12,"丹东市公安局")
worksheet.write(1,13,"元宝分局")
worksheet.write(1,14,"于家派出所")



# 保存文件
old_content.save('jzdr.xls')
