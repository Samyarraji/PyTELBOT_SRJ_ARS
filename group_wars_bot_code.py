import telebot
from telebot import types

BOT_TOKEN = "7955283951:AAHZ8rvCERvk48sHuU-F2u_hP_z6QZZq0bE"
bot = telebot.TeleBot (BOT_TOKEN)


ADMINS_ID = ["6237975392" , "6391649892"]

start_menu = types.ReplyKeyboardMarkup (resize_keyboard=True)
start_menu.row("Shop 🛒" , "Exchange 💱")
start_menu.row("Inventory 🎒" , "Status 📈")
start_menu.row("Mines ⛏️" , "Engage 🪖")
start_menu.row("help 🆘")

#------------------
#Shop
#------------------

shop_menu = types.ReplyKeyboardMarkup (resize_keyboard=True)
shop_menu.row("Air Force ✈️" , "Navy ⚓")
shop_menu.row("Defenses 🛡️")

#------------------
#Air Force
#------------------

air_force_shop = types.ReplyKeyboardMarkup (resize_keyboard=True)
air_force_shop.row("Aviator 🧑‍✈️")
air_force_shop.row("Fighter jets ✈️")
air_force_shop.row("A-Munitions 🎇")

#------------------
#A-Munitions
#------------------

a_munitions_shop = types.ReplyKeyboardMarkup(resize_keyboard=True)
a_munitions_shop.row("A-Bomb 💣")
a_munitions_shop.row("A-Missile 🚀")

#------------------
#Navy
#------------------

navy_shop = types.ReplyKeyboardMarkup(resize_keyboard=True)
navy_shop.row("Naval fleets 🚢")
navy_shop.row("Mariners 🧑‍✈️")
navy_shop.row("B-Munitions 🎇")

#------------------
#B-Munotions
#------------------

b_munitions = types.ReplyKeyboardMarkup(resize_keyboard=True)
b_munitions.row("Torpedoes 🫧")
b_munitions.row("B-Missiles 🚀")

#------------------
#Defenses
#------------------

defense_shop = types.ReplyKeyboardMarkup(resize_keyboard=True)
defense_shop.row("Shield 🛡️")
defense_shop.row("Defense system 🚩")

#------------------
#Handlers </>
#------------------

@bot.message_handler (commands =["start"])
def start (message) :
    print (message.chat.id)
    bot.send_message (message.chat.id , "Choose an option:" , reply_markup=start_menu)

@bot.message_handler (func=lambda m: m.text =="Shop 🛒")
def shop (message) :
    bot.send_message (message.chat.id , "Choose an option: " , reply_markup=shop_menu)

@bot.message_handler (func=lambda m: m.text =="Air Force ✈️")
def air_force_shop_func (message) :
    bot.send_message (message.chat.id , "Choose an option:" , reply_markup=air_force_shop)

@bot.message_handler (func=lambda m: m.text =="A-Munitions 🎇")
def munitions_shop_func (message) :
    bot.send_message (message.chat.id , "Choose an option:" , reply_markup=a_munitions_shop)

@bot.message_handler (func=lambda m: m.text =="Navy ⚓")
def navy_shop_func (message) :
    bot.send_message (message.chat.id , "Choose an option: " , reply_markup=navy_shop)

@bot.message_handler (func=lambda m: m.text =="B-Munitions 🎇")
def b_munitions_func (message):
    bot.send_message (message.chat.id , "Choose an option: " , reply_markup=b_munitions)

@bot.message_handler (func=lambda m: m.text == "Defenses 🛡️")
def defense_shop_func (message):
    bot.send_message(message.chat.id , "Choose an option:" , reply_markup=defense_shop)

print("Bot is running...")
bot.polling(non_stop=True)