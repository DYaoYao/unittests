



import os
import smtplib
from email import encoders
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

from common import readConfig
from common.getHttp import getLog
localReadConfig = readConfig.ReadConfig()

def sendEmail(htmlreport_path):

    #读取配置文件中的邮件信息

    mail_host = localReadConfig.get_email('mail_host')
    mail_port = localReadConfig.get_email('mail_port')
    from_mail = localReadConfig.get_email('from_mail')
    to_mail = localReadConfig.get_email('to_mail')
    password = localReadConfig.get_email('password')
    cc_mail = localReadConfig.get_email('cc_mail')

    #获取html测试报告的路径
    #htmlreport_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),"report")
    #获取excel测试报告的路径
    excelreport_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),"excelReport")
    #判断是否存在report目录
    if os.path.exists(htmlreport_path):

        #构造附件1，html报告

        #获取最后一个html测试报告的名字
        htmlReportname = os.listdir(htmlreport_path)[-1]
        #拼接最后一个html测试报告的路径和名字
        htmlReportDir = os.path.join(htmlreport_path,htmlReportname)
        # 发送html报告
        htmlreport =  MIMEApplication(open(htmlReportDir, 'rb').read())
        htmlreport.add_header('Content-Disposition', 'attachment', filename=htmlReportname)

        #构造附件2，excel报告
        # 获取最后一个html测试报告的名字
        excelreportname = os.listdir(excelreport_path)[-1]
        # 拼接最后一个excel测试报告的路径和名字
        excelReportDir = os.path.join(excelreport_path, excelreportname)
        # 发送excel报告
        excelreport = MIMEApplication(open(excelReportDir, 'rb').read())
        excelreport.add_header('Content-Disposition', 'attachment', filename=excelreportname)

        text = MIMEText('测试已完成，测试结果见附件', 'plain', 'utf-8')
        message = MIMEMultipart()
        message.attach(htmlreport)
        message.attach(excelreport)
        message.attach(text)
        reciverlist = [to_mail,cc_mail]

        message['From'] = from_mail
        message['To'] = to_mail
        message['Cc'] = cc_mail

        subject = '自动化测试报告'
        message['Subject'] = Header(subject, 'utf-8')
        try:
            smtpObj = smtplib.SMTP_SSL(mail_host, mail_port)
            smtpObj.login(from_mail,password)
            smtpObj.sendmail(from_mail, reciverlist,message.as_string())
            getLog.log_info("邮件发送成功")
            print("邮件发送成功")
        except smtplib.SMTPException as e:
            getLog.log_info("邮件发送失败")
            print("邮件发送失败")
            getLog.log_info(e)

    else:
        getLog.log_info("邮件无法发送，没有生成报告")
        print("邮件无法发送，没有生成报告")


