import telebot
from telebot import types

BOT_TOKEN = "7955283951:AAHZ8rvCERvk48sHuU-F2u_hP_z6QZZq0bE"
bot = telebot.TeleBot (BOT_TOKEN)


ADMINS_ID = ["6237975392" , "6391649892"]

start_menu = types.ReplyKeyboardMarkup (resize_keyboard=True)
start_menu.row("Shop 🛒" , "Exchange 💱")
start_menu.row("Inventory 🎒" , "Status 📈")
start_menu.row("Mines ⛏️" , "Engage 🪖")
start_menu.row("Help 🆘")

#------------------
#Shop </>
#------------------

shop_menu = types.ReplyKeyboardMarkup (resize_keyboard=True)
shop_menu.row("Air Force ✈️" , "Navy ⚓")
shop_menu.row("Defenses 🛡️")

#------------------
#Air Force
#------------------

air_force_shop = types.ReplyKeyboardMarkup (resize_keyboard=True)
air_force_shop.row("Aviators 🧑‍✈️")
air_force_shop.row("Fighter jets ✈️")
air_force_shop.row("A-Munitions 🎇")

#------------------
#A-Munitions
#------------------

a_munitions_shop = types.ReplyKeyboardMarkup(resize_keyboard=True)
a_munitions_shop.row("A-Bombs 💣")
a_munitions_shop.row("A-Missiles 🚀")

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
#Help Markup
#------------------

help_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
help_markup.row("Information ❓" , "Contact us 💬") 

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
    "Help 🆘" : {"markup": help_markup , "parent" : "start"}
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
    if message.chat.username :
        print("User :",message.chat.id , "with username :" ,f"@{message.chat.username} has started the bot.")
    else :
        print("User :",message.chat.id , "with name :" ,f"{message.chat.first_name} has started the bot.")
    user_state[message.chat.id] = "start"
    bot.send_message(message.chat.id , "Choose an option:" , reply_markup=start_menu)

@bot.message_handler(func=lambda m: True)
def menu_handler (message) :
    if message.text == "Back 🔙" :
        current_menu = user_state.get (message.chat.id , "start")
        parent = MENUS[current_menu]["parent"]
        if parent :
            user_state [message.chat.id] = parent
            bot.send_message(message.chat.id , "Choose an option:" , reply_markup=MENUS[parent]["markup"])
        else :
            bot.send_message(message.chat.id , "❌ Invalid request.\nPlease start again using /start ")
    elif message.text in MENUS :
        user_state[message.chat.id] = message.text
        bot.send_message(message.chat.id , "Choose an option:" , reply_markup=MENUS[message.text]["markup"])
    elif message.text == "Information ❓" :
        bot.send_message(message.chat.id , "There is no information yet.")
    elif message.text == "Contact us 💬" :
        bot.send_message(message.chat.id , "Write your message down here 👇:")
        bot.register_next_step_handler(message , help_message)
    else :
        bot.send_message(message.chat.id , "❌ Invalid request.")


#------------------
#Functions
#------------------

def help_message (message) :
    for admin_id in ADMINS_ID :
        if message.chat.username :
            bot.send_message (admin_id , f"User: {message.chat.id} with @{message.chat.username} username said:\n\n{message.text}")
        else :
            bot.send_message(admin_id , f"User {message.chat.id} with {message.chat.first_name} username said:\n\n{message.text}")
    bot.send_message(message.chat.id , "Your message has been sent successfully. ✅")

print("Bot is running...")
bot.polling(non_stop=True)