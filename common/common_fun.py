from baseView.baseView import  BaseView
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
import time,os
import csv
from common.desired_caps import appium_desired

class common(BaseView):

    updatebtn=(By.ID,'android:id/button1')
    def check_update_msg(self):
        logging.info('=============check_update_msg===========')
        try:
            self.driver.find_element(*self.updatebtn)
            logging.info('发现更新版本提示')
        except NoSuchElementException:
            logging.info('no update button')
            pass
        else:
            self.driver.find_element(*self.updatebtn).click()
            self.driver.keyevent(4)

    def get_size(self):
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        return x,y

    def swipeleft(self):
        l = self.get_size()
        x1=int(l[0]*0.9)
        y1=int(l[1]*0.5)
        x2=int(l[0]*0.1)
        self.swipe(x1,y1,x2,y1,500)

    def swiperight(self):
        l = self.get_size()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.swipe(x2, y1, x1, y1, 1000)

    def swipeup(self):
        l = self.get_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.8)
        y2 = int(l[1] * 0.2)
        self.swipe(x1,y1,x1,y2,1000)

    def swipedown(self):
        l = self.get_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.8)
        y2 = int(l[1] * 0.2)
        self.swipe(x1,y2,x1,y1,1000)

    def get_time(self):
        self.now=time.strftime("%Y-%m-%d %H-%M-%S")
        return self.now

    def createcurrentdatedir(self):
        date = time.strftime("%Y-%m-%d")
        dirname=os.path.dirname(os.path.dirname(__file__))+'/reports/testresultimg'+date
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        return dirname

    def add_screenshot_to_report(self,testcase):
        date=time.strftime("%Y-%m-%d")
        picfile=os.path.dirname(os.path.dirname(__file__))+'/reports/testresultimg/%s_%s.png' %(testcase,date)
        picfile=os.path.join(self.createcurrentdatedir(),'%s.png'%testcase)
        self.driver.get_screenshot_as_file(picfile)
        print("<img src='" + "./testresultimg"+date+"/%s.png" %testcase + "' width=600 />")

    def getscreenshot(self,module):
        time=self.get_time()
        image_file=os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png' %(module,time)
        logging.info('get %s screenshot' %module)
        self.driver.get_screenshot_as_file(image_file)

    def get_csv_data(self,csv_file,line):
        '''
               获取csv文件指定行的数据
               :param csv_file: csv文件路径
               :param line: 数据行数
               :return:
               '''
        logging.info('=====get_csv_data======')
        with open(csv_file,'r',encoding='utf-8-sig') as file:
            reader=csv.reader(file)
            for index,row in enumerate(reader,1):
                if index==line:
                    return row

    def find_toast_element(self,message):
        formatmessage = '//*[@text=\'{}\']'.format(message)
        toast_element = WebDriverWait(self.driver, 5, 0.2).until(lambda x:x.find_element_by_xpath(formatmessage))
        return toast_element


    def input(self,inputstr,*loc):
        return self.find_element(*loc).send_keys(inputstr)

    def click(self,*loc):
        return self.find_element(*loc).click()

    def switch_to_context(self,contextname):
        return self.driver.switch_to.context(contextname)

    def clear(self,*loc):
        oldtext=self.find_element(*loc).text
        self.driver.keyevent(123)  # 123代表光标移动到末尾键
        for i in range(0, len(oldtext)):
            self.driver.keyevent(67)

    def long_press(self,sec,*loc):
        elem=self.find_element(*loc)
        TouchAction(self.driver).long_press(el=elem,x=None,y=None,duration=1000*int(sec)).release().perform()


if __name__=='__main__':
    driver= appium_desired()
    c=common(driver)
    c.get_size()











