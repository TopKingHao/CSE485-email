
import smtplib

from email.mime.text import MIMEText

from email.header import Header
def send_email(msg):
    
    from_addr = 'droppabled@gmail.com'
    password = 'nqsrsedaewgikfrm'
    
    
    to_addr = 'rdillon3@asu.edu'

    smtp_server = 'smtp.gmail.com'


    msg = MIMEText(msg, 'plain', 'utf-8')

    msg['From'] = Header('Automated Hydroponic System')  
    msg['To'] = Header('Ryan')  
    subject = 'PPM nutrient TDS nutrient level low'
    msg['Subject'] = Header(subject, 'utf-8')


    try:
        smtpobj = smtplib.SMTP_SSL(smtp_server)
        # 
        smtpobj.connect(smtp_server, 465)    
        # 
        smtpobj.login(from_addr, password)   
        # 
        smtpobj.sendmail(from_addr, to_addr, msg.as_string()) 
        print("email send successful")
    except smtplib.SMTPException as e:
        print("email send failed")
        print(e)
    finally:
        # 
        smtpobj.quit()

send_email('')
