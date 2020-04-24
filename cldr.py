from xls import Property
import xlwt
from xlutils.copy import copy
import xlrd

workbook = xlwt.Workbook(encoding = 'ascii')
workbook = xlwt.Workbook(encoding = 'utf-8')
workbook = xlrd.open_workbook("io_xls/cldr.xls")
# 对数据表格进行复制
old_content = copy(workbook)
worksheet = old_content.get_sheet(0)
# 实例化类
dh = Property()

# 调用类中的方法
license = dh.license()
education = dh.education()
lt= dh.local_time()
nt = dh.number_three()
channel = dh.channel()

# 导入excel
worksheet.write(1,0,license)
worksheet.write(1,1,lt)
worksheet.write(1,2,lt)
worksheet.write(1,3,channel)
worksheet.write(1,4,channel)
worksheet.write(1,5,nt)
worksheet.write(1,6,education)
worksheet.write(1,7,"丹东市公安局")
worksheet.write(1,8,"元宝分局")
worksheet.write(1,9,"于家派出所")

# 保存文件
old_content.save('cldr.xls')
