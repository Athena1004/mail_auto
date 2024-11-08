import smtplib
import string
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.application import MIMEApplication # 用于添加附件


host_server = 'smtp.qq.com'  
sender_qq = '1184803185@qq.com' 
pwd = 'vxwoukudgciujffg'
receiver = ['1184803185@qq.com','zxy825308434@foxmail.com','athena@hpecsemi.com','280485939@qq.com']
mail_title = 'Python自动发送html格式的邮件' 

mail_content = "test"

msg = MIMEMultipart()
msg["Subject"] = Header(mail_title,'utf-8')
msg["From"] = sender_qq
msg["To"] = Header("test mail title","utf-8")

msg.attach(MIMEText(mail_content,'plain','utf-8'))
attachment = MIMEApplication(open('./test.xlsx','rb').read())
attachment["Content-Type"] = 'application/octet-stream'
# 给附件重命名
basename = "test.xlsx"
attachment.add_header('Content-Dispositon','attachment',filename=('utf-8', '', basename))#注意：此处basename要转换为gbk编码，否则中文会有乱码。
msg.attach(attachment)


try:
    smtp = SMTP_SSL(host_server) # ssl登录连接到邮件服务器
    smtp.set_debuglevel(1) 
    smtp.ehlo(host_server) 
    smtp.login(sender_qq,pwd)
    smtp.sendmail(sender_qq,receiver,msg.as_string())
    smtp.quit()
    print("send ok")
except smtplib.SMTPException:
    print("send error")

