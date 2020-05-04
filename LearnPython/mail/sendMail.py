import smtplib
from email.mime.text import MIMEText

#   UZULAWTWUZVCXDTH

SMTPServer = "smtp.163.com"

sender = "why674974090@163.com"
##授权码
passwd = "UZULAWTWUZVCXDTH"

message = "a email from python"#邮件正文
msg = MIMEText(message)#转换为msg格式
msg["Subject"] = "learn python"#邮件主题
msg["From"] = sender#发送者

mailServer = smtplib.SMTP(SMTPServer, 25)#发送服务器
mailServer.login(sender, passwd)#登录邮箱
mailServer.sendmail(sender, ["whywuliao@hotmail.com","wanghaoyu2020@gmail.com"], msg.as_string())#发送
mailServer.quit()
