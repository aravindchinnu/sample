from flask import Flask,request
import json
import sys
import requests
import json
#from Flask_Server.Send_PushNotification import SendPushNotification
app = Flask(__name__)

@app.route('/PushNotification',methods = ['POST'])
def send_push_notification():
    input_params = request.form.to_dict()
    if input_params is not None and isinstance(input_params,dict) :
        import requests
        import json

        """serverToken = 'AAAAZZhiaKM:APA91bHQRW2wjzDuL66NIgYtiDu2Zz0kPv1Jt8MvVyyeFD_m5IZO8_j_5CJVvWgXO6aSEMgplPpoBTBAws2zEPM1yotS3IjH23MZsRBUhNEgCWtyjRUvDxlD9EFZLAIOL2nohCWjDZ3-'
        deviceToken = 'cBxjZvyfWf8:APA91bFzRT0qRNvAGipKBIsu4zehexTmU-c4GjUDKBazo87ypsb-_N9ha8v1KHruYRa40RPun7azFpIzN5Rc7vsFCLjcggUan2-Ve6O3Qsj2F3cPhp-hu3H5017V2Xkr0T9WtzQelAo-'
        """
        serverToken = 'AAAAZZhiaKM:APA91bHQRW2wjzDuL66NIgYtiDu2Zz0kPv1Jt8MvVyyeFD_m5IZO8_j_5CJVvWgXO6aSEMgplPpoBTBAws2zEPM1yotS3IjH23MZsRBUhNEgCWtyjRUvDxlD9EFZLAIOL2nohCWjDZ3-
        #serverToken = input_params.get('serverToken')
        deviceToken = input_params.get('deviceToken')
        LociiFlag = input_params.get('LociiFlag')
        if LociiFlag is None or LociiFlag not in ['yes','no']:
            return json.dumps({'status': 'failure'})

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'key=' + serverToken,
        }

        body = {
            'notification': {'title': 'Sending push form python script',
                             'body': 'Hi user avail the exiting offers from this **** store'
                             },
            'to': deviceToken,
            'priority': 'high',
            #   'data': dataPayLoad,
        }
        response = requests.post("https://fcm.googleapis.com/fcm/send", headers=headers, data=json.dumps(body))
        return response.json() 
    else:
        return json.dumps({'status': 0})

if __name__ == '__main__':
    app.run()




