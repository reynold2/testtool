import smtplib
from  email.mime.text import MIMEText
from  email.mime.multipart import MIMEMultipart
from  email.header import Header


#�������������
smtpserver=""
#���������ַ
receiver=""
#���������ַ
sender=""
#���������û�������
user=''
password=""
#�ʼ�����
subject=''
#���͸���
sendfile=""



html=MIMEText(mail_body,"html","utf-8")
html["subject"]=Header("�Զ������Ա���","utf-8")
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



