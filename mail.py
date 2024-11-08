import smtplib
import string
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.application import MIMEApplication

host_server = 'smtp.qq.com'
sender_qq = '1184803185.com'
pwd = 'vxwoukudgciujffg'
receiver = '1184803185.com'
mail_title = 'mailToAthena'


#邮件正文内容
mail_content = "hello athena, how are you lately"

msg = MIMEMultipart()
msg["Subject"] = Header(mail_title,'utf-8')
msg["From"] = sender_qq
msg["To"] = ";".join(receiver)

msg.attach(MIMEText(mail_content,'plain','utf-8'))
#attachment = MIMEApplication(open('./end_code.txt','rb').read())
#attachment["Content-Type"] = 'application/octet-stream'
# 给附件重命名
#basename = "end_code.txt"
#attachment.add_header('Content-Disposition','attachment',filename=('utf-8', '', basename))#注意：此处basename要转换为gbk编码，否则中文会有乱码。
#msg.attach(attachment)


try:
    smtp = SMTP_SSL(host_server) # ssl登录
    #smtp = smtplib.STMP(host_server,25) # ssl登录连接到邮件服务器
    smtp.set_debuglevel(1) # 0是关闭，1是开启debug
    smtp.ehlo(host_server) 
    smtp.login(sender_qq,pwd)
    smtp.sendmail(sender_qq,receiver,msg.as_string())
    smtp.quit()
    print("邮件发送成功")
except smtplib.SMTPException:
    print("无法发送邮件")

