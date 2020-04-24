from xls import Property
import xlwt
from xlutils.copy import copy
import xlrd

workbook = xlwt.Workbook(encoding = 'ascii')
workbook = xlwt.Workbook(encoding = 'utf-8')
workbook = xlrd.open_workbook("io_xls/gndr.xls")
# 对数据表格进行复制
old_content = copy(workbook)
worksheet = old_content.get_sheet(0)

# 实例化类
dh = Property()

# 调用类中的方法
name = dh.name()
telephone = dh.telephone()
identity = dh.identity()
create_job_time = dh.local_time()
sex =dh.sex()
room_number = dh.number_three()
area = dh.area()
pay = dh.pay()
ranges = dh.ranges()

# 导入excel
worksheet.write(1,0,name)
worksheet.write(1,1,sex)
worksheet.write(1,2,identity)
worksheet.write(1,3,telephone)
worksheet.write(1,4,"阳光海运花园")
worksheet.write(1,5,'4A')
worksheet.write(1,6,room_number)
worksheet.write(1,7,create_job_time)
worksheet.write(1,8,area)
worksheet.write(1,9,pay)
worksheet.write(1,10,"丹东市公安局")
worksheet.write(1,11,"元宝分局")
worksheet.write(1,12,"于家派出所")

# 保存文件
old_content.save('gndr.xls')
