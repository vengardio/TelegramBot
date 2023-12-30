import telebot
import config
import time
from telebot import types

bot = telebot.TeleBot(config.TOKEN)
global istexting
istexting = False
global towho
towho = "name"

def to_logs_message(message):
    with open("log.txt", "a", encoding='utf-8') as logs: #write user message to logs
        newLine = "\n" + time.ctime(time.time()) + " - "  +  str(message.from_user.first_name) + ": " + str(message.text)
        logs.write(newLine)

def to_logs_text(message, text):
    with open("log.txt", "a", encoding='utf-8') as logs: #write user message to logs
        newLine = "\n" + time.ctime(time.time()) + " - "  +  str(message.from_user.first_name) + ": " + str(text)
        logs.write(newLine)

def addUserID(message): #[kate 904480006]
    userHere = False
    with open("users.txt", "r") as users:
        users = users.read()
        usersList = list(users.split("\n"))
    usersList = usersList[:-1]
    for i in range(len(usersList)):
        usersList[i] = list(usersList[i].split())
    for i in range(len(usersList)):
        if '933768614' == usersList[i][1]:
            userHere = True
            break
    if userHere == False:
        with open("users.txt", "a") as users:
            newLine = message.from_user.first_name + " " + str(message.from_user.id) + "\n"
            users.write(newLine)

def takeUserID():
    with open("users.txt", "r") as users:
        users = users.read()
        usersList = list(users.split("\n"))
        for i in range(len(usersList)-1):
            usersList[i] = list(usersList[i].split(" "))
            if towho == usersList[i][0]:
                return usersList[i][1]

@bot.message_handler(commands=['start'])
def main(message):
    to_logs_message(message)
    addUserID(message)
    bot.send_message(message.chat.id, f'<B>Привет, {message.from_user.first_name}, я Борис, тупое сотворение информатики!</B>', parse_mode="html")

@bot.message_handler(commands=['owner'])
def owners_info(message):
    to_logs_message(message)
    addUserID(message)

    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Телеграмм", url="https://t.me/StpdCow")
    btn2 = types.InlineKeyboardButton("GitHub", url="https://github.com/vengardio")
    markup.row(btn1, btn2)
    markup.add(types.InlineKeyboardButton("Написать юзеру", callback_data = "sending"))

    bot.send_message(message.chat.id, f'Вот контактные данные моего создателя', reply_markup=markup)

@bot.message_handler(commands=['stop'])
def stop(message):
    global istexting
    to_logs_message(message)
    istexting = False

@bot.message_handler(content_types=['text'])
def default(message):
    global istexting
    to_logs_message(message)
    addUserID(message)
    if istexting == True:
        bot.send_message(message.chat.id, "Сообщение отправлено!")
        bot.send_message(takeUserID(), message.text)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    global istexting
    if callback.data == "textToUser1":
        towho = 'kate'
        istexting = True
        print(towho)
        print(istexting)
    elif callback.data == "textToUser2":
        towho = ')))'
        istexting = True
        print(towho)
        print(istexting)
    elif callback.data == "sending":
        to_logs_text(callback, "/хочет отправить сообщение/")

        markup2 = types.InlineKeyboardMarkup()
        butuser1 = types.InlineKeyboardButton("kate", callback_data='textToUser1')
        butuser2 = types.InlineKeyboardButton(")))", callback_data='textToUser2')
        markup2.row(butuser1, butuser2)
        bot.send_message(callback.message.chat.id, "Кому пишем?", reply_markup=markup2)

bot.polling(none_stop=True)