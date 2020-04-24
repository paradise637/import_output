from xls import Property
import xlwt
from xlutils.copy import copy
import xlrd

workbook = xlwt.Workbook(encoding = 'ascii')
workbook = xlwt.Workbook(encoding = 'utf-8')
workbook = xlrd.open_workbook("zydr.xls")
# 对数据表格进行复制
old_content = copy(workbook)
worksheet = old_content.get_sheet(0)
# 实例化类
dh = Property()
# 调用类中的方法
name = dh.name()
nation = dh.nation()
telephone = dh.telephone()
identity = dh.identity()
ns = dh.number_seven()
sex = dh.sex()
marry = dh.marry()
collde = dh.collde()
time = dh.local_time()

# 导入excel
worksheet.write(1,0,ns)
worksheet.write(1,1,name)
worksheet.write(1,2,identity)
worksheet.write(1,3,sex)
worksheet.write(1,4,marry)
worksheet.write(1,5,collde)
worksheet.write(1,6,"正常")
worksheet.write(1,7,"沈阳中心医院")
worksheet.write(1,8,time)
worksheet.write(1,9,time)
worksheet.write(1,10,"丹东市公安局")
worksheet.write(1,11,"元宝分局")
worksheet.write(1,12,"于家派出所")



# 保存文件
old_content.save('zydr.xls')
