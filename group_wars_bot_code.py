import telebot
from telebot import types

BOT_TOKEN = "7955283951:AAHZ8rvCERvk48sHuU-F2u_hP_z6QZZq0bE"
bot = telebot.TeleBot (BOT_TOKEN)


ADMINS_ID = ["6237975392" , "6391649892"]


@bot.message_handler (commands =["start"])
def start (message) :
    print (message.chat.id)
    markup = types.ReplyKeyboardMarkup (resize_keyboard=True)
    markup.row("Shop" , "Exchange")
    markup.row("Inventory" , "Status")
    markup.row("Mines" , "Engage")
    markup.row("help")
    bot.send_message (message.chat.id , "Choose an option:" , reply_markup=markup)
print("Bot is running...")
bot.polling(non_stop=True)