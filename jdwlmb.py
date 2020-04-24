from xls import Property
import xlwt
from xlutils.copy import copy
import xlrd
from type import Type



workbook = xlrd.open_workbook("io_xls/jdwlmb.xls")
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
other_name =dh.other_name()
other_telephone = dh.other_telephone()
other_identity = dh.other_identity()
leaderTel = dh.phone()
leaderSN = dh.phone_SN()
police = dh.police()
type_net =ty.type_net()
name_j = ty.name_net()
address = ty.address()


# 导入excel
worksheet.write(1,0,name_j)
worksheet.write(1,1,address)
worksheet.write(1,2,"寄递物流")
worksheet.write(1,3,name)
worksheet.write(1,4,telephone)
worksheet.write(1,5,identity)
worksheet.write(1,6,other_name)
worksheet.write(1,7,other_telephone)
worksheet.write(1,8,other_identity)
worksheet.write(1,9,leaderTel)
worksheet.write(1,10,leaderSN)
worksheet.write(1,11,"丹东市公安局")
worksheet.write(1,12,"元宝分局")
worksheet.write(1,13,"于家派出所")
worksheet.write(1,14,police)
worksheet.write(1,15,other_telephone)
worksheet.write(1,16,"123.40466022491456")
worksheet.write(1,17,"41.833858209692046")
worksheet.write(1,18,type_net)



# 保存文件
old_content.save('io_xls/jdwlmb.xls')
