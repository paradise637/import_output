import random

class Type():
    # 散油类型
    def type_oil(self):
        return random.choice(("中石化", '中石油', "中海油"))

    # 散油单位名称
    def name_oil(self):
        file_name = "type_intdef/oil.txt"
        file = open(file_name, mode='r', encoding="utf-8")
        a = file.readlines()
        return random.choice(a)
        file.close()

    # 文博类型
    def type_wb(self):
        return random.choice(("博物馆", '美术馆', "艺术馆", "文化遗产", "文化馆", "图书馆", "体育训练中心", "演艺团队", "其他"))

    # 文博单位名称
    def name_wb(self):
        file_name = "type_intdef/wb.txt"
        file = open(file_name, mode='r', encoding="utf-8")
        a = file.readlines()
        return random.choice(a)
        file.close()

    # 银行类型
    def type_bank(self):
        return random.choice(("银行", '证券', "保信", "信托", "基金", "其他"))

    # 银行单位名称
    def name_bank(self):
        list = []
        file_name = "type_intdef/bank.txt"
        file = open(file_name, mode='r', encoding="utf-8")
        for i in file.readlines():
            i = i.strip()
            list.append(i)
        return random.choice(list)
        file.close()

    # 医院类型
    def type_hospital(self):
        return random.choice(("综合医院", '中医医院', "中西医结合医院", "民族医院", "专科医院", "妇幼保健院", "疗养院", "卫生院", "其他"))

    # 医院单位名称
    def name_hospital(self):
        list = []
        file_name = "type_intdef/hospital.txt"
        file = open(file_name, mode='r', encoding="utf-8")
        for i in file.readlines():
            i = i.strip()
            list.append(i)
        return random.choice(list)
        file.close()

    # 中小幼类型
    def type_myConpany(self):
        return random.choice(("小学", "幼儿园", "中学"))

    # 中小幼单位名称
    def name_myConpany(self):
        list = []
        file_name = "type_intdef/myConpany.txt"
        file = open(file_name, mode='r', encoding="utf-8")
        for eachline in file.readlines():
            eachline = eachline.strip()
            list.append(eachline)
        return random.choice(list)
        file.close()

    # 高校类型
    def type_school(self):
        return random.choice(("高中", "高校", "职高", "技校", '中专', "特教", "其他"))

    # 高校单位名称
    def name_school(self):
        list = []
        file_name = "type_intdef/school.txt"
        file = open(file_name, mode='r', encoding="utf-8")
        for eachline in file.readlines():
            eachline = eachline.strip()
            list.append(eachline)
        return random.choice(list)
        file.close()

    # 党政机关事业单位类型
    def type_dzjg(self):
        return random.choice(("教育","科学技术","工业和信息化","民族事务",'公安',"国家安全","监察","民政","司法",'财政',"人力资源和社会保障","国土资源","环境保护","住房和城乡建设","交通运输","水利","农业农村","应急管理",'商务',"文化和旅游","国家卫生和计划生育","其他"))

    # 党政机关事业单位名称
    def name_dzjg(self):
        list = []
        file_name = "type_intdef/dzjg.txt"
        file = open(file_name, mode='r', encoding="utf-8")
        for eachline in file.readlines():
            eachline = eachline.strip()
            list.append(eachline)
        return random.choice(list)
        file.close()

    # 重点企业类型
    def type_company(self):
        return random.choice(("农业","工业","服务业","邮电",'通信',"社区服务","批发""零售业","交通运输","建筑及安装业","医疗卫生",'城市建设',"旅游","宾馆","餐饮业","其他"))

    # 重点企业单位名称
    def name_company(self):
        list = []
        file_name = "type_intdef/company.txt"
        file = open(file_name, mode='r', encoding="utf-8")
        for eachline in file.readlines():
            eachline = eachline.strip()
            list.append(eachline)
        return random.choice(list)
        file.close()

    #  网点类型
    def type_net(self):
        return random.choice(("物流", "代办点", "菜鸟驿站"))

    # 寄递物流单位名称
    def name_net(self):
        file_name = "type_intdef/net.txt"
        file = open(file_name, mode='r', encoding="utf-8")
        a = file.readlines()
        return random.choice(a)
        file.close()

    #单位类型
    def type_unit(self):
        return random.choice(("散油","寄递物流","中小幼","高校","医院","银行","文博单位","党政机关事业单位","重点企业","军工企业"))

    #地址
    def address(self):
        list = []
        file_name = "type_intdef/address.txt"
        file = open(file_name, mode='r', encoding="utf-8")
        for eachline in file.readlines():
            eachline = eachline.strip()
            list.append(eachline)
        return random.choice(list)
        file.close()



