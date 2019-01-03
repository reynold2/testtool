import smtplib
from  email.mime.text import MIMEText
from  email.mime.multipart import MIMEMultipart
from  email.header import Header


#发送邮箱服务器
smtpserver=""
#接收邮箱地址
receiver=""
#发送邮箱地址
sender=""
#发送邮箱用户和密码
user=''
password=""
#邮件主题
subject=''
#发送附件
sendfile=""



html=MIMEText(mail_body,"html","utf-8")
html["subject"]=Header("自动化测试报告","utf-8")
open(mail_body)

att=MIMEText(sendfile,'base64','utf-8')
att["content-Disposition"]='attachment';filename='log.txt'
att["content-type"]='application/octet-stream'


msgroot=MIMEMultipart("related")
msgroot["subject"]=subject
msgroot.attach(att)

smtp=smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user,password)
smtp.sendmail(sender,receiver,msgroot.as_string())
smtp.quit()



