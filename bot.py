import telebot
import config
import time 

bot = telebot.TeleBot(config.TOKEN)

def to_logs(message): 
    with open("log.txt", "a", encoding='utf-8') as logs: #write user message to logs
        newLine = "\n" + time.ctime(time.time()) + " - "  +  str(message.from_user.first_name) + ": " + str(message.text)
        logs.write(newLine)

@bot.message_handler(commands=['start'])
def main(message):
    to_logs(message)
    bot.send_message(message.chat.id, f'<B>Привет, {message.from_user.first_name}, я Борис, тупое сотворение информатики!</B>', parse_mode="html")

@bot.message_handler(commands=['id'])
def user_id(message):
    to_logs(message)
    bot.send_message(message.chat.id, f"Your ID:{message.from_user.id}")
    
@bot.message_handler(commands=['git'])
def user_id(message):
    to_logs(message)
    bot.send_message(message.chat.id, "Owner's Git page: https://github.com/vengardio")    

@bot.message_handler(content_types=['text'])
def retype(message):
    to_logs(message)
    bot.send_message(message.chat.id, message.text)
    
@bot.message_handler(content_types=['sticker'])
def retype(message):
    to_logs(message)
    bot.send_message(message.chat.id, "Я не понимаю тебя!!! ")
    
bot.polling(none_stop=True) 