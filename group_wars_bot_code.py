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
#Menu Structure </>
#------------------

MENUS = {"start": {"markup": start_menu, "parent": None},
    "Shop 🛒": {"markup": shop_menu, "parent": "start"},
    "Air Force ✈️": {"markup": air_force_shop, "parent": "Shop 🛒"},
    "A-Munitions 🎇": {"markup": a_munitions_shop, "parent": "Air Force ✈️"},
    "Navy ⚓": {"markup": navy_shop, "parent": "Shop 🛒"},
    "B-Munitions 🎇": {"markup": b_munitions, "parent": "Navy ⚓"},
    "Defenses 🛡️": {"markup": defense_shop, "parent": "Shop 🛒"},
    }

def add_back (menu_name) :
    if MENUS[menu_name] ["parent"] :
        MENUS[menu_name]["markup"].row ("Back 🔙") 
for name in MENUS :
    add_back(name)

#------------------
#Handlers </>
#------------------

user_state = {}

@bot.message_handler(commands="start")
def start(message) :
    user_state[message.chat.id] = "start"
    bot.send_message(message.chat.id , "Choose an option:" , reply_markup=start_menu)

@bot.message_handler(func=lambda m: True)
def menu_handler (message) :
    if message.text == "Back 🔙" :
        current_menu = user_state.get (message.chat.id , "start")
        parent = MENUS[current_menu]["parent"]
        user_state [message.chat.id] = parent
        bot.send_message(message.chat.id , "Choose an option:" , reply_markup=MENUS[parent]["markup"])
    elif message.text in MENUS :
        user_state[message.chat.id] = message.text
        bot.send_message(message.chat.id , "Choose an option:" , reply_markup=MENUS[message.text]["markup"])
    else :
        bot.send_message (message.chat.id , "❌ Invalid request.")

    
print("Bot is running...")
bot.polling(non_stop=True)