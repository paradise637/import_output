from xls import Property
import xlwt
from xlutils.copy import copy
import xlrd

workbook = xlwt.Workbook(encoding = 'ascii')
workbook = xlwt.Workbook(encoding = 'utf-8')
workbook = xlrd.open_workbook("io_xls/jdwlsjdr.xls")
# 对数据表格进行复制
old_content = copy(workbook)
worksheet = old_content.get_sheet(0)
# 实例化类
dh = Property()
# 调用类中的方法
name = dh.name()
telephone = dh.telephone()
number_logistics = dh.number_logistics()
weight = dh.weight()
packing = dh.packing()
leaderTel = dh.leaderTel()
other_name = dh.other_name()
other_tel = dh.other_telephone()
company_lg = dh.company_logistics()
ranges =dh.ranges()


# 导入excel
worksheet.write(1,0,number_logistics)
worksheet.write(1,1,weight)
worksheet.write(1,2,packing)
worksheet.write(1,3,name)
worksheet.write(1,4,telephone)
worksheet.write(1,5,leaderTel)
worksheet.write(1,6,other_name)
worksheet.write(1,7,other_tel)
worksheet.write(1,8,"")
worksheet.write(1,9,"工业设备广场")
worksheet.write(1,10,'')
worksheet.write(1,11,company_lg)
worksheet.write(1,12,"丹东市公安局")
worksheet.write(1,13,"元宝分局")
worksheet.write(1,14,"于家派出所")



# 保存文件
old_content.save('jdwlsjdr.xls')
