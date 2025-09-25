import telebot


BOT_TOKEN = "7955283951:AAHZ8rvCERvk48sHuU-F2u_hP_z6QZZq0bE"
bot = telebot.TeleBot (BOT_TOKEN)


ADMINS_ID = ["6237975392" , "6391649892"]


@bot.message_handler (commands =["start"])
def start (message) :
    print (message.chat.id)
    if str(message.chat.id) in ADMINS_ID :
        bot.send_message (message.chat.id , "Admin detected.")
    else :
        bot.send_message (message.chat.id , "Normal user detected.")

print("Bot is running...")
bot.polling(non_stop=True)