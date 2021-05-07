import mail
import line
import psql
import datetime
from time import sleep
from flask import Flask, render_template, request
from threading import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')  

@app.route("/SendMail", methods=["POST"])
def SendMail():
    dt_now = datetime.datetime.now()
    mail_address = str(request.form.get('Mail'))
    user_name = str(request.form.get('Name'))
    message_subject = str(request.form.get('Subject'))
    message_text = str(request.form.get("Text"))
    time = dt_now.strftime('%Y年%m月%d日 %H:%M:%S')

    #MAIL.PY
    check = mail.send_mail(mail_address,"[Pet Cube]お問い合わせ内容の送信完了",f"{user_name}様のお問い合わせ内容が正常に送信されました。回答まで今しばらくお待ちください。",time)
    
    if check == True:
        #PostgreSQL
        db_append = psql.add(mail_address,user_name,message_subject,message_text)
        if db_append == True:
            #--------------送信完了時に表示させるメッセージ-----------------------------------------
            text_log = f"お問い合わせ内容の送信が完了しました。"  
            #------------------------------------------------------------------------------------
            #LINE.PY
            line.line(f"{user_name}様からのお問い合わせ 件名:{message_subject} お問い合わせ内容:{message_text}","")
    else:
        text_log = "お問い合わせ内容の送信に失敗しました。"  
    return render_template('thankyou.html',text_log=text_log,time_now=time)  

if __name__ == "__main__":
    app.run(debug=True)

