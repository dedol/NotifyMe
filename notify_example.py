import json
import requests

def notify(text):
    user = 330303423
    token = '557bf448d4b15bd86a5e08a0a8c705d9'
    r = requests.get('http://notify.dedol.ru/send', params={'user': user, 
                                                            'token': token, 
                                                            'text': text})
    if r.json()['status'] == 'ok':
        return True
    return False


notify('Hello from Python!')