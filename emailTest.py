import zmail

server = zmail.server('1184803185@qq.com','vxwoukudgciujffg')
mail = server.get_latest()
# zmail.show(mail)
print(mail['subject'])
print(mail['id'])
print(mail['from'])
print(mail['to'])
print(mail['content_text'])
print(mail['content_html'])

# 用来保存附件
# target_path为None则默认保存在当前目录下
# overwrite=True 是指如果出现同名文件则进行覆盖
zmail.save_attachment(mail,target_path=None,overwrite=True)
