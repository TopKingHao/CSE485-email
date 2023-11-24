# smtplib 用于邮件的发信动作
import smtplib
# email 用于构建邮件内容
from email.mime.text import MIMEText
# 构建邮件头
from email.header import Header
def send_email(msg):
    # 发信方的信息，这里用google邮箱发送吧
    # 这里需要填入你的google邮箱地址和密码
    from_addr = 'hzhen3@asu.edu'
    password = 'cebtvniaeynkodkx'
    # 收信方邮箱
    #to_addr = 'xxx@asu.edu  他的邮箱'
    to_addr = '2752604849@qq.com'
    # 发信服务器
    smtp_server = 'smtp.gmail.com'

    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    msg = MIMEText(msg, 'plain', 'utf-8')
    # 邮件头信息
    msg['From'] = Header('Hao Zhen ')  # 发送者
    msg['To'] = Header('ryanryan8731')  # 接收者
    subject = 'warning_messgae'
    msg['Subject'] = Header(subject, 'utf-8')  # 邮件主题

    try:
        smtpobj = smtplib.SMTP_SSL(smtp_server)
        # 建立连接
        smtpobj.connect(smtp_server, 465)    
        # 登录
        smtpobj.login(from_addr, password)   
        # 发送邮件
        smtpobj.sendmail(from_addr, to_addr, msg.as_string()) 
        print("email send successful")
    except smtplib.SMTPException as e:
        print("email send failed")
        print(e)
    finally:
        # 关闭服务器
        smtpobj.quit()

send_email('')
