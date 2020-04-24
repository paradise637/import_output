from xls import Property
import xlwt
from xlutils.copy import copy
import xlrd
from type import Type


workbook = xlrd.open_workbook("io_xls/dzjgmb.xls")
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
police =dh.police()
leaderTel =dh.phone()
leaderSN =dh.phone_SN()
name_d =ty.name_dzjg()
add_d = ty.address()
type_d = ty.type_dzjg()

# 导入excel
worksheet.write(1,0,name_d)
worksheet.write(1,1,add_d)
worksheet.write(1,2,"党政机关事业单位")
worksheet.write(1,3,type_d)
worksheet.write(1,4,"重点XXX")
worksheet.write(1,5,safety)
worksheet.write(1,6,name)
worksheet.write(1,7,telephone)
worksheet.write(1,8,identity)
worksheet.write(1,9,leaderTel)
worksheet.write(1,10,leaderSN)
worksheet.write(1,11,"丹东市公安局")
worksheet.write(1,12,"元宝分局")
worksheet.write(1,13,"于家派出所")
worksheet.write(1,14,police)
worksheet.write(1,15,telephone)
worksheet.write(1,16,'123.40466022491456')
worksheet.write(1,17,'41.833858209692046')



# 保存文件
old_content.save('io_xls/dzjgmb.xls')
