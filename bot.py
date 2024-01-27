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
    with open("TelegramBot-main\\log.txt", "a", encoding='utf-8') as logs: #write user message to logs
        newLine = "\n" + time.ctime(time.time()) + " - "  +  str(message.from_user.first_name) + ": " + str(message.text)
        logs.write(newLine)

def to_logs_text(message, text):
    with open("TelegramBot-main\\log.txt", "a", encoding='utf-8') as logs: #write user message to logs
        newLine = "\n" + time.ctime(time.time()) + " - "  +  str(message.from_user.first_name) + ": " + str(text)
        logs.write(newLine)

def addUserID(message): #[kate 904480006]
    userHere = False
    with open("TelegramBot-main\\users.txt", "r") as users:
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
        with open("TelegramBot-main\\users.txt", "a") as users:
            newLine = message.from_user.first_name + " " + str(message.from_user.id) + "\n"
            users.write(newLine)

def returnUserList():
    with open("TelegramBot-main\\users.txt", "r") as users:
        users = list(users.read().split("\n"))
        users = users[:-1]
        userList = {}
        for i in range(len(users)):
            users[i] = list(users[i].split(" "))
            userList[users[i][0]] = int(users[i][1])
    return userList

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
    global towho
    to_logs_message(message)
    addUserID(message)
    if istexting == True:
        bot.send_message(message.chat.id, "Сообщение отправлено!")
        bot.send_message(returnUserList()[towho], message.text)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    global istexting
    global towho
    if callback.data == "textToUser1":
        towho = 'kate'
        to_logs_text(callback, "/хочет отправить сообщение kate/")
        istexting = True
    elif callback.data == "textToUser2":
        to_logs_text(callback, "/хочет отправить сообщение )))/")
        towho = ')))'
        istexting = True
    elif callback.data == "sending":
        markup2 = types.InlineKeyboardMarkup()
        butuser1 = types.InlineKeyboardButton("kate", callback_data='textToUser1')
        butuser2 = types.InlineKeyboardButton(")))", callback_data='textToUser2')
        markup2.row(butuser1, butuser2)
        bot.send_message(callback.message.chat.id, "Кому пишем?", reply_markup=markup2)

bot.polling(none_stop=True)