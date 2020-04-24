import random
import time

class Property:
    #生成姓名
    def name(self):
        xing = '赵张钱孙李周吴郑王冯陈卫蒋沈韩杨谢邹喻柏水窦章云苏潘葛陈范彭郎鲁韦昌刘王黄朱于马苗凤方俞任袁柳鲍史唐费薛雷贺倪汤赫连皇甫澹濮淳孙钟长丘'
        zhong = '东南西北明名民杨超才斯思雅元一下雪月语响地溪端学河强'
        ming = '振震众汝进水圣蛙萨睿宸达姆可乐学恺铭贤超琪天东问景中昂日磊运国界杰达博伟'
        X = random.choice(xing)
        H = random.choice(zhong)
        M = random.choice(ming)
        for i in range(1):
            return X+H+M
    #其他名字
    def other_name(self):
        xing = '赵钱孙李周吴郑王冯陈卫蒋沈韩杨谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳鲍史唐费薛雷贺倪汤赫连皇甫尉迟公羊澹台公冶濮淳于单于叔申屠公孙仲孙令钟离宇文长孙慕容鲜于闾丘司徒司空丌官司子车'
        zhong = '东南西北明名民杨超才斯思雅元一下雪月语响地溪端学河强'
        ming = '振震众汝进水圣蛙萨睿宸达姆可乐学恺铭贤超琪天东问景中昂日磊运国界杰达博伟'
        X = random.choice(xing)
        H = random.choice(zhong)
        M = random.choice(ming)
        for i in range(1):
            return X + H + M

    # 生成性别
    def sex(self):
        return random.choice(("男","女"))

    # 生成民族
    def nation(self):
        return random.choice(("维吾尔族", "壮族","汉族"))

    #电话号码
    def telephone(self):
        return random.randint(13000000000,19999999999)

    #其他号码
    def other_telephone(self):
        return random.randint(13000000000,19999999999)

    #身份证
    def identity(self):
        return random.randint(100000000000000000,999999999999999999)

    #其他身份证
    def other_identity(self):
        return random.randint(100000000000000000, 999999999999999999)

    # 出生日期
    def birthday(self):
        year = random.randint(1960,2000)
        month = random.randint(1,12)

    # 判断每个月有多少天随机生成日
        if year%4 ==0:
            if month in (1,3,5,7,8,10,12):
                day = random.randint(1,31)
            elif month in (4,6,9,11):
                day = random.randint(1,30)
            else:
                day = random.randint(1,29)
        else:
            if month in (1,3,5,7,8,10,12):
                day = random.randint(1,31)
            elif month in (4,6,9,11):
                day = random.randint(1,30)
            else:
                day = random.randint(1,28)
        # 小于10的月份前面加0
        if month < 10:
            month = '0' + str(month)
        if day < 10:
            day = '0' + str(day)
        birthday = str(year)+"-"+str(month)+"-"+str(day)
        return birthday

    #药品类型
    def type_medicine(self):
        return random.choice(("西药","中药"))

    # 户籍地址

    #单位名称

    # 现在居住的地址

    # 所属单位

    # 保安公司

    #文化程度
    def education(self):
        i=random.randint(0,5)
        if i == 0:
            return "本科"
        elif i == 1:
            return "小学"
        elif i == 2:
            return "高中"
        elif i == 3:
            return "博士"
        else:
            return"初中"

    #职称
    def professional(self):
        i=random.randint(0,5)
        if i == 0:
            return "高级工程师"
        elif i == 1:
            return"中级工程师"
        elif i == 2:
            return "初级工程师"
        elif i == 3:
            return "保安总监"
        else:
            return "工程师"

    #获取当前的时间(入职时间，就诊时间)
    def local_time(self):
        localstime = time.strftime("%Y-%m-%d ", time.localtime())
        return localstime

    # 生成市局，分局，派出所
    # def ranges(self):
    #     i=random.randint(0,4)
    #     if i == 0:
    #         return
    #         worksheet.write(1,13,'丹东市公安局')
    #         worksheet.write(1, 14, '元宝分局派出所')
    #         worksheet.write(1, 15, '于家派出所')
    #     elif i == 1:
    #         return
    #         worksheet.write(1,13,'沈阳市公安局')
    #         worksheet.write(1,14,'铁西分局')
    #         worksheet.write(1,15,'启工派出所')
    #     elif i == 2:
    #         return
    #         worksheet.write(1, 13, '大连市公安局')
    #         worksheet.write(1, 14, '旅顺口分局')
    #         worksheet.write(1, 15, '铁三派出所')
    #     elif i == 3:
    #         return
    #         worksheet.write(1,13,'丹东市公安局')
    #         worksheet.write(1, 14, '合作区分局')
    #         worksheet.write(1, 15, '安民派出所')

    #车牌号码
    def license(self):
        area = '辽鲁京'
        number = ('34632',"21344","23456")
        X = random.choice(area)
        H = random.choice(number)
        for i in range(1):
            return X + H


    #进场时间

    #出场时间

    #进场通道

    #出场通道

    #安装地点
    def local(self):
        return random.choice(("门口", "走廊", "四周"))


    # 基础设备规模
    def size(self):
        return random.choice(("小型", "中型", "大型"))

    #重点等级
    def grade(self):
        return random.choice(("三级","二级","一级"))

    #安全等级
    def safety(self):
        return random.choice(("省级","市级","县级","其他"))

    #单位联系电话
    def phone(self):
        dian = ['024-', '0415-', '0411-']
        hua = ['25400768', '82269228', '88907091']
        X = random.choice(dian)
        H = random.choice(hua)
        for i in range(1):
            return X+H

    #单位传真号码
    def phone_SN(self):
        dian = ['024-', '0415-', '0411-']
        hua = ['25400768', '82269228', '88907091']
        X = random.choice(dian)
        H = random.choice(hua)
        for i in range(1):
            return X+H

    #经度

    #纬度

    #设备编号

    #挂号诊所

    #入网面积

    #本年度实缴

    #专业名称


    #常见证件名称
    def documents(self):
        i = random.randint(0, 2)
        if i == 0:
            return "居民身份证"
        else:
            return "护照"



    #证件号码

    #学制
    def eductional_system(self):
        return random.choice(("五年", "四年", "三年"))

    #学院名称
    def college(self):
        i = random.randint(0, 3)
        if i == 0:
            return "基础教育学院"
        elif i == 1:
            return "国际教育学院"
        elif i == 2:
            return "管理学院"

    #常见证件代码
    def identity_code(self):
        i = random.randint(0, 4)
        # 代表身份证
        if i == 0:
            return "111"
        # 代表临时居民身份证
        elif i == 1:
            return "112"
        # 代表户口簿
        elif i == 2:
            return "113"
        # 代表中国解放军军管证
        elif i == 3:
            return "114"
        # 代表普官证
        elif i == 4:
            return "115"
        # 代表暂住证
        elif i == 5:
            return "116"
        # 代表普官证
        else:
            return "117"

    #基础设施
    def base(self):
        return random.choice(("摄像头", "路灯","水龙头","报警器"))


    #现居住地址
    def address_now(self):
        province = '辽宁省'
        city = '丹东市'
        county = random.choice(("各庄村", '皮村村', '东村', '曹备庄', '康营家园', '下辛堡社区', '孙河村', '康营村', '北甸东', '北甸西', '西甸村', '下辛堡',
                                '上辛堡村', '黄港村', '李县坟', '雷桥村', '沈家坟', '沙子营', '第沟村'))
        number = random.randint(00, 100)
        return province + city + county + str(number) + "号"

    #网点类型

    #寄递物流公司
    def company_logistics(self):
        return random.choice(("韵达", "中通","圆通","顺丰"))

    #就诊科室
    def collde(self):
        return random.choice(("五官急诊科", "急诊内科","急诊外科","皮肤急诊科"))

    #药品名称

    #药品类型

    #使用气数

    #缴纳费用

    #民警
    def police(self):
        return random.choice(("陈民警", "张民警","刘民警","王民警"))

    #简要案情

    #部门
    def department(self):
        return random.choice(("开发", '测试', "运维"))

    #重点部位

    #重点单位类型
    #卡ID

    #出入口
    def passway(self):
        return random.choice(("南门", "东门","西门","北门"))

    #进/出
    def io(self):
        return random.choice(("进", "出"))

    #入学时间
    def time_school(self):
        return random.choice(("20150601", "20150901","20160601",'20170601','20180601'))

    # 案件号

    # 住院症状

    # 民族代码
    def nation_code(self):
        return random.choice(("1", "2", "3"))

    # 性别代码
    def sex_code(self):
        return random.choice(("1", "2"))

    # 包装用品
    def packing(self):
        return random.choice(("箱子", '塑料袋', "木架"))

    # 婚姻状况（病人）
    def marry(self):
        return random.choice(("已婚", "未婚"))

    #进场通道出场通道
    def channel(self):
        return random.choice(("A1", "A2","B1","B2","C1","C2"))


    # 入网面积 使用气数
    def area(self):
         return random.randint(40.0,200.0)

    # 本年度实缴
    def pay(self):
         return random.randint(300,1000)

    # 实际重量
    def number_two(self):
        return random.randint(0, 100)

    # 房间号,就诊科室
    def number_three(self):
         return random.randint(000,999)

    # 设备编号
    def number_seven(self):
        return random.randint(0000000, 9999999)

    # 物流编号,表名，
    def number_thirteen(self):
        return random.randint(1000000000000, 99999999999999)

    # 执照许可证登记号
    def number_fifteen(self):
        return random.randint(100000000000000, 999999999999999)













