from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
import pytz
from datetime import datetime
import telebot
token = ''

chat_id= ''
bot = telebot.TeleBot(token)

# Define o fuso horário de São Paulo
saopaulo_tz = pytz.timezone('America/Sao_Paulo')

main_process = None

def execute_main():
    global main_process
    try:
        main_process = subprocess.Popen(['python', 'play.py'])
        print("play.py está sendo executado...")
        entrada= f'''🚀VAMOS COMEÇAR🚀'''
        bot.send_message(chat_id=chat_id,
                     text=entrada,
                     parse_mode='HTML',
                     disable_web_page_preview=True)    
    except Exception as e:
        print("Erro ao executar main.py:", e)

def schedule_tasks():
    scheduler = BlockingScheduler(timezone=saopaulo_tz)

    # Agende as tarefas utilizando o método `scheduler.add_job`
    scheduler.add_job(execute_main, 'cron', hour=10, minute=0)  # Executa às 10:00 AM
    scheduler.add_job(job_finishing, 'cron', hour=11, minute=0)  # Executa às 11:00 AM
    scheduler.add_job(execute_main, 'cron', hour=14, minute=0)  # Executa às 15:16 PM
    scheduler.add_job(job_finishing, 'cron', hour=15, minute=0)  # Executa às 16:00 PM
    scheduler.add_job(execute_main, 'cron', hour=20, minute=0)  # Executa às 20:00 PM
    scheduler.add_job(job_finishing, 'cron', hour=21, minute=0)  # Executa às 22:00 PM

    scheduler.start()

def job_finishing():
    global main_process
    try:
        if main_process is not None:
            main_process.kill()
            main_process = None
            print("play.py foi finalizado.")
            entrada2= f'''🚀FINALIZAMOS COM SALDO POSITIVO🚀'''
            bot.send_message(chat_id=chat_id,
                     text=entrada2,
                     parse_mode='HTML',
                     disable_web_page_preview=True)    
    except Exception as e:
        print("Erro ao finalizar main.py:", e)

if __name__ == "__main__":
    schedule_tasks()
