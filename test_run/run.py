# -*- coding:utf-8 -*-
import unittest
from BeautifulReport import BeautifulReport
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import time,logging
import sys
import os
import zipfile

now = time.strftime('%Y-%m-%d %H_%M_%S')
date = time.strftime("%Y-%m-%d")

def report():
    logging.info('开始执行')
    path = 'C:\\Users\\Administrator\\PycharmProjects\\shequapp\\'
    sys.path.append(path)
    # testdir= '../testcase'
    testdir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'testcase')
    # reportdir='../reports'
    reportdir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'reports')
    discover = unittest.defaultTestLoader.discover(testdir, pattern='test_capturebyhand.py', top_level_dir=None)
    report_name = now + 'test_report.html'
    result = BeautifulReport(discover)
    result.report(filename=report_name, description='智慧社区测试报告', report_dir=reportdir)

def zipDir(dirpath,outFullName):
    logging.info('开始压缩测试报告和截图')
    """
    压缩指定文件夹:param dirpath: 目标文件夹路径；:param outFullName: 压缩文件保存路径+xxxx.zip；:return: 无
    """
    zip = zipfile.ZipFile(outFullName,"w",zipfile.ZIP_DEFLATED)
    htmlreport=os.path.dirname(os.path.dirname(__file__)) + '/reports/'+now + 'test_report.html'
    for path,dirnames,filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath,'testresultimg'+date+'/')

        for filename in filenames:
            zip.write(os.path.join(path,filename),os.path.join(fpath,filename))
        zip.write(htmlreport,now + 'test_report.html')
    zip.close()

def sendmail():
    logging.info('执行发送报告邮件')
    # 发送邮件登录、发送人、收件人、主题、邮件正文、附件等参数准备
    smtpserver = 'smtp.qq.com'
    user = '413266269@qq.com'
    password = 'DX0610750'
    sender = '413266269@qq.com'
    receivers = ['xieys@zjshenyue.cn','413266269@qq.com']
    subject = ' 智慧社区APP测试报告' + now
    mailbody = ' 大家好，智慧社区app本次自动化测试结果如下，请下载附件查看详细报告和截图'
    msg = MIMEText(mailbody, 'plain', 'utf-8')
    # 开始组装邮件收件人、发件人、正文
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = ','.join(receivers)
    message['Subject'] = subject
    message.attach(msg)
    #开始组装报告附件
    resultzip = MIMEText(
        open('C:\\Users\\Administrator\\PycharmProjects\\shequapp\\test_run\\'+'shequAPP_report'+now+'.zip', 'rb').read(),
        'base64', 'utf-8')  # 测试结果压缩文件作为附件
    resultzip["Content-Type"] = 'application/octet-stream'
    resultzip["Content-Disposition"] = 'attachment; filename="shequAPP_report'+now+'.zip"'
    message.attach(resultzip)
    # 执行发送邮件
    try:
        # smtpObj = smtplib.SMTP()
        # smtpObj.connect(smtpserver, 25)
        smtpObj = smtplib.SMTP_SSL(smtpserver, 465)
        smtpObj.login(user, 'bkievlqenpilbjfj')
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        raise e


if __name__ == '__main__':
    report()

    dirname = os.path.dirname(os.path.dirname(__file__)) + '/reports/testresultimg' + date
    zipDir(dirname,'shequAPP_report'+now+'.zip')

    sendmail()







