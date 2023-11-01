import telebot
import sys

class bot:
    def token(token, mode):
        if token == "":
            raise TypeError("\033[37m pygroupbot token must not be a null")
            print("\033[0m")
        elif mode == "":
            raise TypeError("\033[37m pygroupbot mode must not be a null")
            print("\033[0m")

        else:
            global bot
            bot = telebot.TeleBot(token, parse_mode=mode)

def start_message(start_msg):
    @bot.message_handler(commands=["start"]) 
    def send_message(message):
        bot.reply_to(message, start_msg)

def menu_message(menu_msg):
    @bot.message_handler(commands=["menu"]) 
    def send_message(message):
        bot.reply_to(message, menu_msg)

def help_message(help_msg):
    @bot.message_handler(commands=["help"]) 
    def send_message(message):
        bot.reply_to(message, help_msg)

def info_message(info_msg):
    @bot.message_handler(commands=["info"]) 
    def send_message(message):
        bot.reply_to(message, info_msg + "\n\nCreated with PyGroupBot Library...")


def kick_message(kick_msg):
    @bot.message_handler(commands=["kick"]) 
    def send_message(message):
        if message.chat.type == 'private':  # Check if chat is private
            bot.reply_to(message, "This is a private chat. Kicking users is only allowed in group chats.")
            return

        replied_message = message.reply_to_message
    
        if replied_message is None:  # If no message is replied to
            bot.reply_to(message, "You must reply to a message to kick the user.")
            return

        kicked_user = replied_message.from_user.id
        kicker_user = message.from_user.id

        if kicked_user == kicker_user:
            bot.reply_to(message, "Do you want to kick yourself? What happened to this world?")
        elif kicked_user == bot.get_me().id:
            bot.reply_to(message, "Why do I need to kick myself?")
        else:
            if bot.get_chat_member(message.chat.id, message.from_user.id).status in ["creator", "administrator"]:
                try:
                    bot.kick_chat_member(message.chat.id, kicked_user)
                    bot.reply_to(message, kick_msg)
                except Exception as errkick:
                    print("bot hasn't admin rights. ERROR_523")
            else:
                bot.reply_to(message, "You're not an admin of this group")





def ban_message(ban_msg):
    @bot.message_handler(commands=["ban"]) 
    def send_message(message):
        if message.chat.type == 'private':  # Check if chat is private
            bot.reply_to(message, "This is a private chat. Banning users is only allowed in group chats.")
            return

        replied_message = message.reply_to_message
    
        if replied_message is None:  # If no message is replied to
            bot.reply_to(message, "You must reply to a message to ban the user.")
            return

        baned_user = replied_message.from_user.id
        baner_user = message.from_user.id

        if baned_user == baner_user:
            bot.reply_to(message, "Do you want to ban yourself? What happened to this world?")
        elif baned_user == bot.get_me().id:
            bot.reply_to(message, "Why do I need to ban myself?")
        else:
            if bot.get_chat_member(message.chat.id, message.from_user.id).status in ["creator", "administrator"]:
                try:
                    bot.ban_chat_member(message.chat.id, baned_user)
                    bot.reply_to(message, kick_msg)
                except Exception as errkick:
                    print("bot hasn't admin rights. ERROR_523")
            else:
                bot.reply_to(message, "You're not an admin of this group")

def unban_message(unban_msg):
    @bot.message_handler(commands=["unban"])
    def send_message(message):
        if message.chat.type == 'private':  # Check if chat is private
            bot.reply_to(message, "This is a private chat. Unbanning users is only allowed in group chats.")
            return

        replied_message = message.reply_to_message
    
        if replied_message is None:  # If no message is replied to
            bot.reply_to(message, "You must reply to a message to unban the user.")
            return

        unbaned_user = replied_message.from_user.id
        unbaner_user = message.from_user.id

        if unbaned_user == unbaner_user:
            bot.reply_to(message, "You're not banned right now!")
        elif unbaned_user == bot.get_me().id:
            bot.reply_to(message, "Dude! I'm not banned!")
        else:
            if bot.get_chat_member(message.chat.id, message.from_user.id).status in ["creator", "administrator"]:
                try:
                    bot.unban_chat_member(message.chat.id, unbaned_user)
                    bot.reply_to(message, kick_msg)
                except Exception as errkick:
                    print("bot hasn't admin rights. ERROR_523")
            else:
                bot.reply_to(message, "You're not an admin of this group")


def run(bool_value):
    if bool_value == True:
        try:
            print("\033[32m PyGroupBot Server Started - Bot is Running...") 
            print("\033[0m")
            bot.polling(none_stop= True)
        except Exception as errpol:
            print("\033[31m Bad request from telegram API. [Cannot run bot. Check your internet connection]. ERROR_400")
            print("\033[0m")

    elif bool_value == False:
        print("\033[33m PyGroupBot Server Not Started Yet - Bot is Offline...")
        print("\033[0m")
        sys.exit()

    else:
        raise TypeError("\033[37m .run() only need boolean value!")
        print("\033[0m")
        sys.exit()
        