import telebot
import requests

TOKEN = '596253902:AAHhHYhE9pRxKwOCtQzI87-Yj1xr0WYhfzU'
MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'
payload = {}
def post_data():
    #'reply_to_message_id': 3
    payload['chat_id'] = 141945723,
    payload['text'] = 'post data method'

    req = requests.post(f'{MAIN_URL}/sendMessage', data=payload)
    print(req.json())

def get_data():
    payload['offset'] = 0
    #payload['limit'] = 1
    #payload['timeout'] = 0
    req = requests.post(f'{MAIN_URL}/getUpdates', data=payload)
    repidm = req.json()['result'][0]['message']['message_id']
    payload.clear()
    payload['reply_to_message_id'] = repidm
    post_data()
    print(req.json())


if __name__ == '__main__':
    get_data()
    #post_data()
