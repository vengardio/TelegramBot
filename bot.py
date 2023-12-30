import telebot
import config
import time 
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

def to_logs_message(message): 
    with open("log.txt", "a", encoding='utf-8') as logs: #write user message to logs
        newLine = "\n" + time.ctime(time.time()) + " - "  +  str(message.from_user.first_name) + ": " + str(message.text)
        logs.write(newLine)
        
def to_logs_text(message, text): 
    with open("log.txt", "a", encoding='utf-8') as logs: #write user message to logs
        newLine = "\n" + time.ctime(time.time()) + " - "  +  str(message.from_user.first_name) + ": " + str(text)
        logs.write(newLine)

@bot.message_handler(commands=['start'])
def main(message):
    to_logs_message(message)
    bot.send_message(message.chat.id, f'<B>Привет, {message.from_user.first_name}, я Борис, тупое сотворение информатики!</B>', parse_mode="html")

@bot.message_handler(commands=['owner'])
def owners_info(message):
    to_logs_message(message)

    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Телеграмм", url="https://t.me/StpdCow")
    btn2 = types.InlineKeyboardButton("GitHub", url="https://github.com/vengardio")
    markup.row(btn1, btn2)
    markup.add(types.InlineKeyboardButton("А я просто кнопка)", callback_data = "button_answer"))
    
    bot.send_message(message.chat.id, f'Вот контактные данные моего создателя', reply_markup=markup)
    
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == "button_answer":
        to_logs_text(callback, "/нажал на тупую кнопку/")
        bot.send_message(callback.message.chat.id, "ну и что, ну нажал ты, что дальше то?")

@bot.message_handler(content_types=['text'])
def default(message):
    to_logs_message(message)
    
bot.polling(none_stop=True) 