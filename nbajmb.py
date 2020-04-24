from xls import Property
import xlwt
from xlutils.copy import copy
import xlrd
from type import Type


workbook = xlrd.open_workbook("io_xls/nbajmb.xls")
# 对数据表格进行复制
old_content = copy(workbook)
worksheet = old_content.get_sheet(0)
# 实例化类
dh = Property()
ty = Type()


# 调用类中的方法
name = dh.name()
ns = dh.number_seven()
lt = dh.local_time()
name_n = ty.type_hospital()

# 导入excel
worksheet.write(1,0,ns)
worksheet.write(1,1,"斗殴")
worksheet.write(1,2,name_n)
worksheet.write(1,3,"打架")
worksheet.write(1,4,lt)
worksheet.write(1,5,"聚集斗殴")
worksheet.write(1,6,"丹东市公安局")
worksheet.write(1,7,"元宝分局")
worksheet.write(1,8,"于家派出所")


# 保存文件
old_content.save('io_xls/nbajmb.xls')
