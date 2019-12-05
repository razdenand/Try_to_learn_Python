import requests
import time
from datetime import datetime
 
BITCOIN_PRICE_THRESHOLD = 10000
BITCOIN_API_URL = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
Etherium_URL = 'https://api.coinmarketcap.com/v1/ticker/ethereum/'
IFTTT_WEBHOOKS_URL = 'https://maker.ifttt.com/trigger/{}/with/key/pC6_AiSBqxPF2qLXrhpEZ0soip09M1F5PNhXYoKeg-B'

def get_value_of_bitcoin():
    val = requests.get(BITCOIN_API_URL)
    val_json = val.json()
    return(val_json[0]['price_usd'])

def get_value_of_etherium():
    val = requests.get(Etherium_URL)
    val_json = val.json()
    return(val_json[0]['price_usd'])

def post_ifttt_webhook(event, value1, value2):
    data1 = {'value1': value1,
             'value2' : value2}
    ifttt_event_url = IFTTT_WEBHOOKS_URL.format(event)  # Вставка желаемого события
    requests.post(ifttt_event_url, json=data1)  # Отправка запроса HTTP POST в URL вебхука
 
def format_bitcoin_history(bitcoin_history):
    rows = []
    for bitcoin_price in bitcoin_history:
        date = bitcoin_price['date'].strftime('%d.%m.%Y %H:%M')  # Форматирует дату в строку: '24.02.2018 15:09'
        price = bitcoin_price['price']
        row = '{}: $<b>{}</b>'.format(date, price)
        rows.append(row)
 
    
    return '<br>'.join(rows)
 
def main():
    bitcoin_history = []
    etherium_history = []
    while True:
        price_bitcoin = get_value_of_bitcoin()
        price_etherium = get_value_of_etherium()
        date = datetime.now()
        bitcoin_history.append({'date': date, 'price': price_bitcoin})
        etherium_history.append({'date' :date, 'price': price_etherium})
        # Отправка уведомления в Telegram
        if len(bitcoin_history) == 2:  
            post_ifttt_webhook('bitcoin_and_etherium_price_update', format_bitcoin_history(bitcoin_history), format_bitcoin_history(etherium_history))
            # Сброс истории
            bitcoin_history = []
            etherium_history = []
 
        time.sleep(60)   
if __name__ == '__main__':
    main()
