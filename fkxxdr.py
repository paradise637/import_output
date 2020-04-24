from xls import Property
from xlutils.copy import copy
import xlrd
from type import Type

workbook = xlrd.open_workbook("io_xls/fkxxdr.xls")
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
create_job_time = dh.local_time()
safety =dh.safety()
equipment_number =dh.number_three()
name_f = ty.name_company()
name_b = ty.name_dzjg()
na = dh.other_name()


# 导入excel
worksheet.write(1,0,name)
worksheet.write(1,1,telephone)
worksheet.write(1,2,"面试")
worksheet.write(1,3,identity)
worksheet.write(1,4,nation)
worksheet.write(1,5,"简历")
worksheet.write(1,6,name_f)
worksheet.write(1,7,create_job_time)
worksheet.write(1,8,create_job_time)
worksheet.write(1,9,name_b)
worksheet.write(1,10,na)
worksheet.write(1,11,equipment_number)
worksheet.write(1,12,"丹东市公安局")
worksheet.write(1,13,"元宝分局")
worksheet.write(1,14,"于家派出所")

# 保存文件
old_content.save('io_xls/fkxxdr.xls')
