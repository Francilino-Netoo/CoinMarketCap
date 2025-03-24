import time
import websocket
import json
import os
from colorama import Fore
if os.name == 'nt':
    import colorama
    colorama.init()

'''
{
  "d": {
    "id": 1975 ID da cripto
    "p": Preço atual
    "p24h": Variação percentual nas últimas 24h
    "p7d": Variação percentual nos últimos 7 dias
    "p30d": Variação percentual nos últimos 30 dias
    "p3m": Variação percentual nos últimos 3 meses
    "p1y": Variação percentual no último ano
    "pytd": Variação percentual no ano até agora
    "pall": Preço histórico máximo
    "as": Oferta circulante
    "mc": Market cap (valor total de mercado)
    "fmc24hpc": Mudança percentual do market cap nas últimas 24h
  },
  "t": Timestamp
  "c": Canal de origem da atualização
}
'''
def valor1(ws, message):
    try:
        json_message = json.loads(message)
        if 'd' in json_message:
            typ1 = json_message['d']['id']
            if typ1 == 1975:
                p = json_message['d']['p']
                p24h = json_message['d']['p24h']
                p7d = json_message['d']['p7d']
                p30d = json_message['d']['p30d']
                p3m = json_message['d']['p3m']
                p1y = json_message['d']['p1y']
                pytd = json_message['d']['pytd']
                pall = json_message['d']['pall']
                ass = json_message['d']['as']
                mc = json_message['d']['mc']
                fmc24hpc = json_message['d']['fmc24hpc']
                
                print('p:', p, 'p24h:', p24h, 'p7d:', p7d, 'p30d:', p30d, 'p3m:', p3m,'p1y:', p1y, 'pytd:', pytd, 'pall:', pall, 'ass:', ass, 'mc:', mc, 'fmc24hpc:', fmc24hpc)
    except Exception as e:
        #print(Fore.RED + "[ERRO] Falha ao processar valor1:", str(e) + Fore.RESET)
        pass

def valor2(ws, message):
    try:
        json_message = json.loads(message)
        if 'd' in json_message:
            typ1 = json_message['d']['id']
            if typ1 == 6536:
                p = json_message['d']['p']
                v = json_message['d']['v']
                p1h = json_message['d']['p1h']
                p24h = json_message['d']['p24h']
                p7d = json_message['d']['p7d']
                p30d = json_message['d']['p30d']
                mc = json_message['d']['mc']
                d = json_message['d']['d']
                vd = json_message['d']['vd']
                
                print('p:', p, 'v:', v, 'p1h:', p1h, 'p24h:', p24h, 'p7d:', p7d,'p30d:', p30d, 'mc:', mc, 'd:', d, 'vd:', vd)
    except Exception as e:
        #print(Fore.RED + "[ERRO] Falha ao processar valor2:", str(e) + Fore.RESET)
        pass

def on_message(ws, message):
    try:
        valor1(ws, message)
        valor2(ws, message)
    except Exception as e:
        print(Fore.RED + "Error:", str(e) + Fore.RESET)

def on_open(ws):
    print(Fore.GREEN + "[INFO] Conectado ao WebSocket" + Fore.RESET)
    ws.send(json.dumps({"method": "RSUBSCRIPTION", "params": ["main-site@crypto_price_5s@{}@normal",
                                                              "1,1027,52,825,5426,6536,1975"]}))

def on_close(ws, close_status_code, close_msg):
    time.sleep(1)
    conectar_websocket()

def conectar_websocket():
    ws = websocket.WebSocketApp(
        "wss://push.coinmarketcap.com/ws?device=web&client_source=home_page",
        on_message=on_message,
        on_close=on_close,
        header={"Origin": "https://coinmarketcap.com",
                "Referer": "https://coinmarketcap.com",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    )
    ws.on_open = on_open
    ws.run_forever()

if __name__ == "__main__":
    conectar_websocket()
