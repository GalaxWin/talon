import telebot
import time
from datetime import datetime, timedelta
import pytz
import random

# Defina o fuso horário para Brasília
timezone = pytz.timezone('America/Sao_Paulo')

token = '6685045831:AAGf9AwyO1U08O90otaWvh6VPmcXr4L9jeo'  
chat_id = '-1002037182328' 

bot = telebot.TeleBot(token)

# Lista com os títulos disponíveis
titulos = [
  '🐯 <a href="https://galaxwin.bet?c=Kanibal">FORTUNE TIGER</a>',
  '🐮 <a href="https://galaxwin.bet?c=Kanibal">FORTUNE OX</a>',
  '🐭 <a href="https://galaxwin.bet?c=Kanibal">FORTUNE MOUSE</a>',
  '🐰 <a href="https://galaxwin.bet?c=Kanibal">FORTUNE RABITT</a>',
  
]

# Índice inicial para escolher o primeiro título da lista
indice_titulo = 0

while True:
  try:
    # Obtém a hora atual em Brasília
    current_time = datetime.now(timezone)

    # Adiciona 3 minutos ao tempo atual
    expiration_time = current_time + timedelta(minutes=2)

    # Formata a hora como uma string legível
    expiration_time_str = expiration_time.strftime('%H:%M')
    nu1 = random.randrange(2, 9)
    nu2 = random.randrange(2, 9)
    finalizada = '✅✅GREEN✅✅'

    # Escolher o próximo título da lista
    titulo_atual = titulos[indice_titulo]

    entrada = f'''💰 Entrada Confirmada 💰
{titulo_atual}
🕑 <b>Válido até:</b> {expiration_time_str} 
👉 <b>{nu1}x Normal</b>
⚡️ <b>{nu2}x Turbo</b>
🚥 <b>Intercalando</b>
🔗<a href="https://galaxwin.bet?c=Kanibal"><b>CADASTRE-SE & JOGUE!!!</b></a>'''

    bot.send_message(chat_id=chat_id,
                     text=entrada,
                     parse_mode='HTML',
                     disable_web_page_preview=True)
    print('msg enviada')
    time.sleep(120)
    bot.send_message(chat_id=chat_id,
                     text=finalizada,
                     parse_mode='HTML',
                     disable_web_page_preview=True)
    print('msg green enviada')
    time.sleep(300)

    # Avançar para o próximo título na lista
    indice_titulo = (indice_titulo + 1) % len(titulos)

  except Exception as e:
    print(f'Ocorreu um erro: {e}')
    print('Reiniciando o código...')
    time.sleep(10)
    continue
