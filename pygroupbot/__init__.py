import telebot
import sys

class bot:
    def token(token, mode):
        if token == "":
            raise TypeError("PyGroupBot token must not be empty")
        elif mode == "":
            raise TypeError("PyGroupBot mode must not be empty")
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
            if message.chat.type == "private":
                bot.reply_to(message, "Kicking is only allowed in groups!")
            else:
                if bot.get_chat_member(message.chat.id, message.from_user.id).status in ["creator", "administrator"]:
                    if message.reply_to_message:
                        try:
                            kicks = message.reply_to_message.from_user.id
                            bot.kick_chat_member(message.chat.id, kicks)
                            bot.reply_to(message, kick_msg)
                        except Exception as errkick:
                            print("Something Wrong. ERROR_523")
                    else:
                        bot.reply_to(message, "Reply to a message from a user to kick them")
                else:
                    bot.reply_to(message, "You're not an admin of this group")

def ban_message(ban_msg):
        @bot.message_handler(commands=["ban"]) 
        def send_message(message):
            if message.chat.type == "private":
                bot.reply_to(message, "Banning is only allowed in groups!")
            else:
                if bot.get_chat_member(message.chat.id, message.from_user.id).status in ["creator", "administrator"]:
                    if message.reply_to_message:
                        try:
                            bans = message.reply_to_message.from_user.id
                            bot.kick_chat_member(message.chat.id, bans)
                            bot.reply_to(message, ban_msg)
                        except Exception as errkick:
                            print("Something Wrong. ERROR_523")
                    else:
                        bot.reply_to(message, "Reply to a message from a user to ban them")
                else:
                    bot.reply_to(message, "You're not an admin of this group")

def unban_message(unban_msg):
        @bot.message_handler(commands=["unban"]) 
        def send_message(message):
            if message.chat.type == "private":
                bot.reply_to(message, "Unbanning is only allowed in groups!")
            else:
                if bot.get_chat_member(message.chat.id, message.from_user.id).status in ["creator", "administrator"]:
                    if message.reply_to_message:
                        try:
                            unbans = message.reply_to_message.from_user.id
                            bot.unban_chat_member(message.chat.id, unbans)
                            bot.reply_to(message, unban_msg)
                        except Exception as errkick:
                            print("Something Wrong. ERROR_523")
                    else:
                        bot.reply_to(message, "Reply to a message from a user to unban them")
                else:
                    bot.reply_to(message, "You're not an admin of this group")

def run(bool_value):
        if bool_value == True:
            try:
                print("PyGroupBot Server Started - Bot is Running...")
                bot.polling(none_stop=True)
                
            except Exception as errpol:
                raise Exception("Bad request from Telegram API. Cannot run bot. Check your internet connection. ERROR_400")

        elif bool_value == False:
            print("PyGroupBot Server Not Started Yet - Bot is Offline...")
            sys.exit()

        else:
            raise TypeError(".run() only needs a boolean value!")
       