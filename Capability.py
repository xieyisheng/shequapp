from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'

# 模拟器
#desired_caps['platformVersion'] = '5.1.1'
# desired_caps['deviceName'] = '127.0.0.1:62025'

#荣耀10真机
desired_caps['paltformVersion'] = '9'
desired_caps['deviceName'] = 'Honor 10'

desired_caps['app'] = r'D:\apps\zhsq_1.6.3_358.apk'
desired_caps['appPackage'] = 'com.ygwy'
desired_caps['appActivity'] = 'com.ygwy.MainActivity'
desired_caps['automationName']='uiautomator2'

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)