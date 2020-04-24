import random
# # # dian = ['024-','0415-','0411-']
# # # hua = ['25400768','82269228','88907091']
# # # X = random.choice(dian)
# # # H = random.choice(hua)
# # # for i in range(4):
# #
# # # print(random.randint(0000000,9999999))
# #
# #
# # # def identity(self):
# # # print( random.randint(40.0,200.0))
# #
# #
# # def address(self):
# # province = '辽宁省'
# # city = '丹东市'
# # county = random.choice((",'第沟村'))
# # number = random.randint(00,100)
# # print(province + city + county + str(number)+"号")
# # # print(type(number))
#
#
list = []
file_name = "type_intdef/school.txt"
file = open(file_name, mode='r', encoding="utf-8")
for eachline in file.readlines():
    eachline = eachline.strip()
    list.append(eachline)
# print(list)
a = random.choice(list)
print(a)
    # print(eachline)
    # print(eachline)
    # b = random.choice(list)
    # print(b)
#     a = filter(lambda ch: ch not in "\n", eachline)
    # a = list(file.readlines())
# b = list(filter(lambda ch:ch not in "\n ",a))
# b = list(a)
# c = file.readlines(b)
# print(random.choice(b))

# file_name = "type_intdef/dzjg.txt"
# file = open(file_name, mode='r', encoding="utf-8")
# a = file.readlines()
# c = a.strip()
# b = list(filter(lambda ch: ch not in "\n ", a))
# return random.choice(b)
# file.close()
# file.close()
