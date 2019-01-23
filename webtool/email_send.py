# -*- coding: UTF-8 -*-
#！usr/bin/python
import smtplib
from  email.mime.text import MIMEText
from  email.header import Header
from  email.mime.multipart import MIMEMultipart
from  webtool.log_config import LOGER
def send_mail(content_filename,accessory_filename=None):
    try:
        htmlcontent=open(content_filename, 'rb')
        ZW = MIMEText(htmlcontent.read(), "html","utf-8")
    except IOError:
        LOGER.loginfo(IOError.filename)
    finally:
        htmlcontent.close()
    msgRoot=MIMEMultipart()
    msgRoot['Subject']=Header("邮件测试","utf-8")
    msgRoot['From'] = Header("测试系统", 'utf-8')
    msgRoot['To'] = Header("开发人员", 'utf-8')
    msgRoot.attach(ZW)
    if accessory_filename:
        try:
            fujiancontent = open(accessory_filename, 'rb')
            FJ = MIMEText(fujiancontent.read(), 'base64', 'utf-8')
        except:
            LOGER.loginfo("附件文件打开异常")
        finally:
            fujiancontent.close()
        FJ["Content-Type"] = 'application/octet-stream'
        FJ["Content-Disposition"] = 'attachment; filename="%s"'%accessory_filename
        msgRoot.attach(FJ)
    try:
        smtp = smtplib.SMTP()
        smtp.connect("smtp.qq.com")
        smtp.login("www.47812005@qq.com", "rxyriuplwysrbihj")
        smtp.sendmail("www.47812005@qq.com", "1029425458@qq.com", msgRoot.as_string())
        smtp.quit()
        LOGER.loginfo("邮件发送成功")
    except smtplib.SMTPException:
        LOGER.loginfo("Error: 无法发送邮件")
    finally:
        LOGER.loginfo("连接销毁")
if __name__=="__main__":
    send_mail("Report\\2018-12-29 13_59_26_result.html")





