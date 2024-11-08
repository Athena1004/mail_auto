import smtplib
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.application import MIMEApplication
import zmail

# smtplib模块主要负责发送邮件：是一个发送邮件的动作，连接邮箱服务器，登录邮箱，发送邮件（有发件人，收信人，邮件内容）。
# email模块主要负责构造邮件：指的是邮箱页面显示的一些构造，如发件人，收件人，主题，正文，附件等。


host_server = 'smtp.qq.com'  #qq邮箱smtp服务器
sender_qq = '1184803185@qq.com' 
pwd = 'vxwoukudgciujffg'
#receiver = ['1184803185@qq.com','zxy825308434@foxmail.com','athena@hpecsemi.com','280485939@qq.com']
receiver = ['1184803185@qq.com']
mail_title = 'Python自动发送的邮件by Athena' 
mail_content = "python auto send email test" #邮件正文内容
# 初始化一个邮件主体
msg = MIMEMultipart()
msg["Subject"] = Header(mail_title,'utf-8')
msg["From"] = sender_qq
msg['To'] = ";".join(receiver)
# 邮件正文内容
msg.attach(MIMEText(mail_content,'plain','utf-8'))


File = 'D:\\Backup\\桌面\\mail_auto\\end_code.txt'
txt_file = MIMEApplication(open(File, 'rb').read())
txt_file.add_header('Content-Disposition', 'attachment', filename=File)
m = MIMEMultipart('mixed')
m.attach(mail_content)
m.attach(txt_file)

try:
    #smtp = SMTP_SSL(host_server) # ssl登录
    smtp = smtplib.SMTP('smtp.qq.com',25)
    smtp.login(sender_qq,pwd)
    smtp.sendmail(sender_qq,receiver,msg.as_string())
    print("send ok")
    smtp.quit()
    #server = zmail.server('1184803185@qq.com','vxwoukudgciujffg')
    #mail = server.get_latest()
    #zmail.save_attachment(mail,target_path=None,overwrite=True)
    #zmail.show(mail)
except smtplib.SMTPException as e:
    print("send error:",e) 
