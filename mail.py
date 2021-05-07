from email.mime.text import MIMEText
import smtplib

mail_chack=None

def send_mail(mail_address,message_subject,message_text,time):
    msg = MIMEText(message_text,"html")
    msg["Subject"] = message_subject
    msg["To"] = mail_address
    msg["From"] = "---@gmail.com"
    time = time

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        #------メールアドレスとパスワード------
        server.login("---@gmail.com", "---")
        server.send_message(msg)
        server.quit()
        return True
    except:
        return False 

if __name__=='__main__':
    send_mail(mail_address,message_subject,message_text,time)
