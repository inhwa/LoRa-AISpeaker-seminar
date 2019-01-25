import requests
import json
TOKEN = 'INPUT_YOUR_TOKEN' #토큰을 변수에 저장
Bot_URL = "https://api.telegram.org/bot{}/".format(TOKEN)

#먼저 봇에게 아무 메세지나 보내세요 ~!
html = requests.get(Bot_URL+'getUpdates')
print(Bot_URL+'getUpdates')
jsonStr = json.loads(html.text)
chat_id = jsonStr['result'][0]['message']['chat']['id']
chat_url = "https://api.telegram.org/bot{}/sendMessage?chat_id={}".format(TOKEN, chat_id)

while True:
    _text = input(">>> 봇에게 보낼말 : ")
    requests.get(chat_url + '&text='+_text)
