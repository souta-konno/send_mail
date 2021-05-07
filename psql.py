
def add(mail_addres,user_name,subject,message):
    try:
        print(f'DB追加\n{mail_addres},{user_name},{subject},{message}')
        return True
    except:
        print('失敗')
        return False
    
if __name__=='__main__':
    add(mail_addres,user_name,subject,message)