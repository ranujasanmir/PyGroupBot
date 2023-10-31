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
            kicks = message.reply_to_message.from_user.id
            if message.chat.type == "private":
                bot.reply_to(message, "Kicking is only allowed in groups!")
            elif kicks == message.from_user.id:
                bot.reply_to(message, "Why are you trying to kick yourself?")
            elif kicks == bot.get_me().id:
                bot.reply_to(message, "Why I need to kick myself?")

            else:
                if bot.get_chat_member(message.chat.id, message.from_user.id).status in ["creator", "administrator"]:
                    if message.reply_to_message:
                        try:
                            
                            bot.kick_chat_member(message.chat.id, kicks)
                            bot.reply_to(message, kick_msg)
                        except Exception as errkick:
                            raise Exception("bot hasn't admin rights. ERROR_523")
                    else:
                        bot.reply_to(message, "Reply to message from users to kick him")
        
                else:
                    bot.reply_to(message, "You're not an admin of this group")

def ban_message(ban_msg):
    @bot.message_handler(commands=["ban"]) 
    def send_message(message):
            bans = message.reply_to_message.from_user.id
            if message.chat.type == "private":
                bot.reply_to(message, "Banning is only allowed in groups!")
            elif bans == message.from_user.id:
                bot.reply_to(message, "Why are you trying to ban yourself?")
            elif bans == bot.get_me().id:
                bot.reply_to(message, "Why I need to ban myself?")
            else:
                if bot.get_chat_member(message.chat.id, message.from_user.id).status in ["creator", "administrator"]:
                    if message.reply_to_message:
                        try:
                            
                            bot.kick_chat_member(message.chat.id, bans)
                            bot.reply_to(message, ban_msg)
                        except Exception as errkick:
                            raise Exception("bot hasn't admin rights. ERROR_523")
                    else:
                        bot.reply_to(message, "Reply to message from users to ban him")
        
                else:
                    bot.reply_to(message, "You're not an admin of this group")

def unban_message(unban_msg):
    @bot.message_handler(commands=["unban"])
    def send_message(message):
            unbans = message.reply_to_message.from_user.id
            if message.chat.type == "private":
                bot.reply_to(message, "Unbanning is only allowed in groups!")
            elif unbans == message.from_user.id:
                bot.reply_to(message, "Why are you trying to unban yourself. Wait a minute... You're not banned!")
            elif unbans == bot.get_me().id:
                bot.reply_to(message, "I'm not banned like you!")
            else:
                if bot.get_chat_member(message.chat.id, message.from_user.id).status in ["creator", "administrator"]:
                    if message.reply_to_message:
                        try:
                            
                            bot.kick_chat_member(message.chat.id, kicks)
                            bot.reply_to(message, unban_msg)
                        except Exception as errkick:
                            raise Exception("bot hasn't admin rights. ERROR_523")
                    else:
                        bot.reply_to(message, "Reply to message from users to unban him")
        
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
        