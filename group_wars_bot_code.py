import telebot
from telebot import types

BOT_TOKEN = "7955283951:AAHZ8rvCERvk48sHuU-F2u_hP_z6QZZq0bE"
bot = telebot.TeleBot (BOT_TOKEN)


ADMINS_ID = ["6237975392" , "6391649892"]

start_menu = types.ReplyKeyboardMarkup (resize_keyboard=True)
start_menu.row("Shop" , "Exchange")
start_menu.row("Inventory" , "Status")
start_menu.row("Mines" , "Engage")
start_menu.row("help")

#------------------

shop_menu = types.ReplyKeyboardMarkup (resize_keyboard=True)
shop_menu.row("Air Force" , "Navy")
shop_menu.row("Defense")

#------------------

air_force_shop = types.ReplyKeyboardMarkup (resize_keyboard=True)
air_force_shop.row("Aviators")
air_force_shop.row("Fighter jets")
air_force_shop.row("A-Munitions")

#------------------

a_munitions_shop = types.ReplyKeyboardMarkup(resize_keyboard=True)
a_munitions_shop.row("A-Bomb")
a_munitions_shop.row("A-Missile")

#------------------

aviators_shop = types.ReplyKeyboardMarkup (resize_keyboard=True)
aviators_shop.row ("Test Aviator")

#------------------

fighter_jets_shop = types.ReplyKeyboardMarkup(resize_keyboard=True)
fighter_jets_shop.row("Test Plane")

#------------------

navy_shop = types.ReplyKeyboardMarkup(resize_keyboard=True)
navy_shop.row("Naval fleets")
navy_shop.row("Mariners")
navy_shop.row("B-Munitions")

#------------------

b_munitions = types.ReplyKeyboardMarkup(resize_keyboard=True)
b_munitions.row("Torpedoes")
b_munitions.row("B-Missiles")

#------------------

@bot.message_handler (commands =["start"])
def start (message) :
    print (message.chat.id)
    bot.send_message (message.chat.id , "Choose an option:" , reply_markup=start_menu)

@bot.message_handler (func=lambda m: m.text =="Shop")
def shop (message) :
    bot.send_message (message.chat.id , "Choose an option: " , reply_markup=shop_menu)

@bot.message_handler (func=lambda m: m.text =="Air Force")
def air_force_shop_func (message) :
    bot.send_message (message.chat.id , "Choose an option:" , reply_markup=air_force_shop)

@bot.message_handler (func=lambda m: m.text =="Aviators")
def aviators_shop_func (message) :
    bot.send_message (message.chat.id , "Choose an option:" , reply_markup= aviators_shop)

@bot.message_handler (func=lambda m: m.text =="Fighter jets")
def fighter_jets_shop_func (message) :
    bot.send_message (message.chat.id , "Choose an option:" , reply_markup=fighter_jets_shop)

@bot.message_handler (func=lambda m: m.text =="Munitions")
def munitions_shop_func (message) :
    bot.send_message (message.chat.id , "Choose an option:" , reply_markup=a_munitions_shop)

@bot.message_handler (func=lambda m: m.text =="Navy")
def navy_shop_func (message) :
    bot.send_message (message.chat.id , "Choose an option: " , reply_markup=navy_shop)

@bot.message_handler (func=lambda m: m.text =="B-Munitions")
def b_munitions_func (message):
    bot.send_message (message.chat.id , "Choose an option: " , reply_markup=b_munitions)

print("Bot is running...")
bot.polling(non_stop=True)