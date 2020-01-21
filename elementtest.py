from Capability import driver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

driver.implicitly_wait(6)
driver.find_element_by_id('android:id/button1').click()
driver.keyevent(4)
driver.find_element_by_xpath('//android.widget.EditText[@text="请输入手机号/身份证号"]').send_keys('189000000001')
driver.find_element_by_xpath('//android.widget.EditText[@text="请输入登录密码"]').send_keys('111111')
driver.find_element_by_xpath('//android.widget.TextView[@text="立即登录"]').click()


correctmessage = '登录成功'
message='//*[@text=\'{}\']'.format(correctmessage)
toast_element = WebDriverWait(driver,5,0.2).until(lambda x:x.find_element_by_xpath(message))
print(toast_element.text)

driver.find_element_by_id('android:id/button1').click()
driver.keyevent(4)

def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x,y

print(get_size())

def swipeleft():
    l=get_size()
    x1=int(l[0]*0.9)
    y1=int(l[1]*0.22)
    x2=int(l[0]*0.1)
    driver.swipe(x1,y1,x2,y1,500)

def swiperight():
    l=get_size()
    x1=int(l[0]*0.1)
    y1 = int(l[1] * 0.22)
    x2 = int(l[0] * 0.9)
    driver.swipe(x1,y1,x2,y1,500)

for i in range(5):
    swipeleft()
    sleep(0.5)

for i in range(5):
    swiperight()
    sleep(0.5)
