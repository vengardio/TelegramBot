import telebot
import config
import time 

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'])
def lalala(message):
    with open("log.txt", "a", encoding='utf-8') as logs:
        newLine = "\n" + time.ctime(time.time()) + " - "  +  str(message.from_user.first_name) + ": " + str(message.text)
        logs.write(newLine)
    #bot.send_message(message.chat.id, "Извините, мадам, я не могу вам писать, вы занятая дама...")
    bot.send_message(message.chat.id, message.text)
    
bot.polling(none_stop=True) 