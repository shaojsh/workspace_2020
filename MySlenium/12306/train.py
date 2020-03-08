from winsound import Beep

from selenium.webdriver.support.select import Select
import inputdata
import datetime
import time
import myemail
from selenium import webdriver


class buy_tickets:
    def buy_tickets(self, num):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 告知数据源的路径
        path = "C://Users//86176//Desktop//inputData.xlsx"
        # 实例化对象
        inputData = inputdata.ReadExcel(path)
        self.dataList = inputData.dict_data()
        # 登录12306账号
        browser = self.driver.get('https://kyfw.12306.cn/otn/resources/login.html')
        self.driver.find_element_by_css_selector('.login-hd-account').click()

        self.driver.find_element_by_id('J-userName').send_keys(self.dataList[num][0])
        self.driver.find_element_by_id('J-password').send_keys(self.dataList[num][1])
        time.sleep(30)
        # 打开指定网址12306
        self.driver.get("https://kyfw.12306.cn/otn/leftTicket/init")
        # 输入出发地址 伤害
        fromEle = self.driver.find_element_by_id('fromStationText')
        # 先进行点击 12306限制，不点击不行
        fromEle.click()
        fromEle.clear()
        # 字符串拼接
        formData = self.dataList[num][2] + '\n'
        fromEle.send_keys(formData)
        # 输入目的地
        toEle = self.driver.find_element_by_id('toStationText')
        # 先进行点击 12306限制，不点击不行
        toEle.click()
        toEle.clear()
        # 字符串拼接
        formData = self.dataList[num][3] + '\n'
        toEle.send_keys(formData)

        timeSleet = Select(self.driver.find_element_by_id('cc_start_time'))

        timePre = self.dataList[num][4]
        timeSleet.select_by_visible_text(timePre)

        # 得到现在的日期(字符串)
        strNowTime = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d")
        nowTime = datetime.datetime.strptime(strNowTime, "%Y-%m-%d")
        # 得到要抢票的那一天的日期
        fuTime = datetime.datetime.strptime(self.dataList[num][5], '%Y-%m-%d')
        # n天后开始抢票
        day = (fuTime - nowTime).days
        # 选择第n个tag
        tomorrow = self.driver.find_element_by_css_selector('#date_range li:nth-child(' + str(day + 1) + ')')
        time.sleep(2)
        self.isGet = False
        # 记录循环次数
        i = 0
        # 循环不断地检索
        time.sleep(8)
        self.get_ticket(i, tomorrow, num)

    def get_ticket(self, i, tomorrow, num):
        try:
            while True:
                i += 1
                time.sleep(2)
                tomorrow.click()
                # 车的种类
                typeTrain = self.dataList[num][7]
                # 票的种类
                typeTicket = self.dataList[num][6]

                if typeTrain == 'GC-高铁/城际':
                    self.tickTSeat(num, typeTrain, typeTicket)
                elif typeTrain == 'D-动车':
                    self.tickTSeat(num, typeTrain, typeTicket)
                elif typeTrain == 'Z-直达':
                    self.tickTSeat(num, typeTrain, typeTicket)
                elif typeTrain == 'T-特快':
                    self.tickTSeat(num, typeTrain, typeTicket)
                elif typeTrain == 'K-快速':
                    self.tickTSeat(num, typeTrain, typeTicket)
                elif typeTrain == '其他':
                    self.tickTSeat(num, typeTrain, typeTicket)
                if self.isGet:
                    Beep(1500, 5000)
                    print('!!!!!主人，有票了!!!!!')

                    # 选中抢票人信息(切片)
                    i = 1

                    strName1 = "\"" + self.dataList[num][9] + "\""
                    contains = "contains(text()," + strName1 + ")"
                    if len(self.dataList[num]) > 10:
                        for one in self.dataList[num][11:]:
                            strNameI = "\"" + str(one[i]) + "\""
                            contains = contains + " or " + "contains(text()," + strNameI + ")"
                    # 顾客信息选中后提交订单
                    ID = "\"" + 'normal_passenger_id' + "\""
                    xpathCus = "//*[@id=" + ID + "]/li/label[" + contains + "]/../input"
                    cus = self.driver.find_elements_by_xpath(xpathCus)
                    for cu in cus:
                        cu.click()
                    self.driver.find_element_by_css_selector('#submitOrder_id').click()
                    # 抢票
                    self.driver.find_element_by_link_text('确认').click()
                    Beep(1500, 5000)
                    myemail.sendEmail()
                else:
                    print(f'#{i}轮没有找到')
            self.driver.quit()
        except Exception:
            print('被人截胡啦')
            time.sleep(8)
            self.driver.find_element_by_id('query_ticket').click()
            self.get_ticket(i, tomorrow, num)

    def tickType(self, num, theTypeTrains):
        for one in theTypeTrains:
            name = one.text
            # 火车型号
            typeTrain = name[0]
            # 高铁（G）
            if typeTrain == 'G':
                if self.dataList[num][7] == 'GC-高铁/城际':
                    self.isGet = True
                    print('**********有剩余的车票' + name)
                    # 预定按钮的xpath
                    buyXpath = "//a[contains(text(), '" + name + "')]/../../../../../td[13]"
                    self.driver.find_element_by_xpath(buyXpath).click()
                    break
                else:
                    self.isGet = False
            if typeTrain == 'D':
                if self.dataList[num][7] == 'D-动车':
                    self.isGet = True
                    print('**********有剩余的车票' + name)
                    # 预定按钮的xpath
                    buyXpath = "//a[contains(text(), '" + name + "')]/../../../../../td[13]"
                    self.driver.find_element_by_xpath(buyXpath).click()
                    break
                else:
                    self.isGet = False
            if typeTrain == 'Z':
                if self.dataList[num][7] == 'Z-直达':
                    self.isGet = True
                    print('**********有剩余的车票' + name)
                    # 预定按钮的xpath
                    buyXpath = "//a[contains(text(), '" + name + "')]/../../../../../td[13]"
                    self.driver.find_element_by_xpath(buyXpath).click()
                    break
                else:
                    self.isGet = False
            if typeTrain == 'T':
                if self.dataList[num][7] == 'T-特快':
                    self.isGet = True
                    print('**********有剩余的车票' + name)
                    # 预定按钮的xpath
                    buyXpath = "//a[contains(text(), '" + name + "')]/../../../../../td[13]"
                    self.driver.find_element_by_xpath(buyXpath).click()
                    break
                else:
                    self.isGet = False
            if typeTrain == 'K':
                if self.dataList[num][7] == 'K-快速':
                    self.isGet = True
                    print('**********有剩余的车票' + name)
                    # 预定按钮的xpath
                    buyXpath = "//a[contains(text(), '" + name + "')]/../../../../../td[13]"
                    self.driver.find_element_by_xpath(buyXpath).click()
                    break
                else:
                    self.isGet = False
            if typeTrain == 'K' or typeTrain == 'Z' or typeTrain == 'K':
                if self.dataList[num][7] == 'Z/T/K':
                    self.isGet = True
                    print('**********有剩余的车票' + name)
                    # 预定按钮的xpath
                    buyXpath = "//a[contains(text(), '" + name + "')]/../../../../../td[13]"
                    self.driver.find_element_by_xpath(buyXpath).click()
                    break
                else:
                    self.isGet = False

            elif typeTrain != 'G' and typeTrain != 'D' and typeTrain != 'Z' and typeTrain != 'T' and typeTrain != 'K':
                if self.dataList[num][7] == '其他':
                    self.isGet = True
                    print('**********有剩余的车票' + name)
                    # 预定按钮的xpath
                    buyXpath = "//a[contains(text(), '" + name + "')]/../../../../../td[13]"
                    self.driver.find_element_by_xpath(buyXpath).click()
                    break

    def tickTSeat(self, num, typeTrain, typeTicket):
        if typeTicket == '商务座':
            xpathbuss = '//*[@id="queryLeftTable"]//td[2][@class]/../td[1]//a'
            thebussTrains = self.driver.find_elements_by_xpath(xpathbuss)
            self.tickType(num, thebussTrains)
        if typeTicket == '一等座':
            xpathbussSeatOne = '//*[@id="queryLeftTable"]//td[3][@class]/../td[1]//a'
            bussSeatOneTrains = self.driver.find_elements_by_xpath(xpathbussSeatOne)
            self.tickType(num, bussSeatOneTrains)
        if typeTicket == '二等座':
            xpathbussSeatTwo = '//*[@id="queryLeftTable"]//td[4][@class]/../td[1]//a'
            bussSeatTwoTrains = self.driver.find_elements_by_xpath(xpathbussSeatTwo)
            self.tickType(num, bussSeatTwoTrains)
        if typeTicket == '高级软卧':
            xpathdevLaySoft = '//*[@id="queryLeftTable"]//td[5][@class]/../td[1]//a'
            devLaySoftTrains = self.driver.find_elements_by_xpath(xpathdevLaySoft)
            self.tickType(num, devLaySoftTrains)
        if typeTicket == '软卧一等卧铺':
            xpathdevLaySoftOne = '//*[@id="queryLeftTable"]//td[6][@class]/../td[1]//a'
            devLaySoftOneTrains = self.driver.find_elements_by_xpath(xpathdevLaySoftOne)
            self.tickType(num, devLaySoftOneTrains)
        if typeTicket == '动卧':
            xpathLayMove = '//*[@id="queryLeftTable"]//td[7][@class]/../td[1]//a'
            layMoveTrains = self.driver.find_elements_by_xpath(xpathLayMove)
            self.tickType(num, layMoveTrains)
        if typeTicket == '硬卧二等卧铺':
            xpathLay = '//*[@id="queryLeftTable"]//td[8][@class]/../td[1]//a'
            theLayTrains = self.driver.find_elements_by_xpath(xpathLay)
            self.tickType(num, theLayTrains)
        if typeTicket == '软座':
            xpathSeatSoft = '//*[@id="queryLeftTable"]//td[9][@class]/../td[1]//a'
            seatSoftTrains = self.driver.find_elements_by_xpath(xpathSeatSoft)
            self.tickType(num, seatSoftTrains)
        if typeTicket == '硬座':
            xpath = '//*[@id="queryLeftTable"]//td[10][@class]/../td[1]//a'
            theSeatTrains = self.driver.find_elements_by_xpath(xpath)
            self.tickType(num, theSeatTrains)
        if typeTicket == '无座':
            xpathNo = '//*[@id="queryLeftTable"]//td[11][@class]/../td[1]//a'
            theSeatNoTrains = self.driver.find_elements_by_xpath(xpathNo)
            self.tickType(num, theSeatNoTrains)
        if typeTicket == '其他':
            xpathOth = '//*[@id="queryLeftTable"]//td[12][@class]/../td[1]//a'
            othTrains = self.driver.find_elements_by_xpath(xpathOth)
            self.tickType(num, othTrains)
