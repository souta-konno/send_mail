import requests
import argparse

def line(message,image):
    line_log = None
    def lineNotify(message,args):
        try:
            line_notify_api = ''
            line_notify_token = ''
            payload = {'message': message}
            headers = {'Authorization': 'Bearer ' + line_notify_token}
            if len(args) == 0:
                requests.post(line_notify_api, data=payload, headers=headers)
            else:
                files={"imageFile":open(args,"rb")}
                requests.post(line_notify_api, data=payload, headers=headers,files=files)
            return line_log == True
        except:
            print('接続失敗')
            return line_log == False
    if image == True:
        image_url ="picture_data.jpg"
    else:
        image_url =""
    lineNotify(message,image_url)
    return line_log
    
if __name__=='__main__':
    line(message,image)