from xls import Property
import xlwt
from xlutils.copy import copy
import xlrd

workbook = xlwt.Workbook(encoding = 'ascii')
workbook = xlwt.Workbook(encoding = 'utf-8')
workbook = xlrd.open_workbook("io_xls/jzmb.xls")
# 对数据表格进行复制
old_content = copy(workbook)
worksheet = old_content.get_sheet(0)
# 实例化类
dh = Property()
# 调用类中的方法
name = dh.name()
myconpanytype = dh.myConpanyType()
telephone = dh.telephone()
identity = dh.identity()
birthday = dh.birthday()
sex = dh.sex()
collde = dh.collde()
other_name = dh.other_name()
lt = dh.local_time()
ranges = dh.ranges()


# 导入excel
worksheet.write(1,0,name)
worksheet.write(1,1,sex)
worksheet.write(1,2,telephone)
worksheet.write(1,3,identity)
worksheet.write(1,4,birthday)
worksheet.write(1,5,collde)
worksheet.write(1,6,other_name)
worksheet.write(1,7,"丹东市中心医院")
worksheet.write(1,8,lt)
worksheet.write(1,9,"丹东市公安局")
worksheet.write(1,10,"元宝分局")
worksheet.write(1,11,"于家派出所")



# 保存文件
old_content.save('jzmb.xls')
