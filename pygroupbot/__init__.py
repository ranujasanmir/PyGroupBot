import telebot
import sys

def online(start_msg, menu_msg, help_msg, kick_msg, ban_msg, unban_msg, token):
    
    if sys.version_info.major >= 3: # Checking python version

        bot = telebot.TeleBot(token) # Get bot token

        @bot.message_handler(commands=["start"]) # Start command
        def send_message(message):
            bot.reply_to(message, start_msg)

        @bot.message_handler(commands=["menu"]) # Menu command
        def send_message(message):
            bot.reply_to(message, menu_msg)

        @bot.message_handler(commands=["help"]) # Help command
        def send_message(message):
            bot.reply_to(message, help_msg)

        @bot.message_handler(commands=["kick"]) # Kick command
        def send_message(message):
            if bot.get_chat_member(message.chat.id, message.from_user.id).status in ["creator", "administrator"]:
                if message.reply_to_message:
                    try:
                        kicks = message.reply_to_message.from_user.id
                        bot.kick_chat_member(message.chat.id, kicks)
                        bot.reply_to(message, kick_msg)
                    except Exception as errkick:
                        raise Exception("bot hasn't admin rights. ERROR_523")
                else:
                    bot.reply_to(message, "Reply to message from users to kick him")
        
            else:
                bot.reply_to(message, "You're not an admin of this group")

        @bot.message_handler(commands=["ban"]) # Ban command
        def send_message(message):
            if bot.get_chat_member(message.chat.id, message.from_user.id).status in ["creator", "administrator"]:
                if message.reply_to_message:
                    try:
                        bans = message.reply_to_message.from_user.id
                        bot.ban_chat_member(message.chat.id, bans)
                        bot.reply_to(message, ban_msg)
                    except Exception as errkick:
                        raise Exception("bot hasn't admin rights. ERROR_523")
                else:   
                    bot.reply_to(message, "Reply to message from users to ban him")
        
            else:
                bot.reply_to(message, "You're not an admin of this group")


        @bot.message_handler(commands=["unban"]) # Unban command
        def send_message(message):
            if bot.get_chat_member(message.chat.id, message.from_user.id).status in ["creator", "administrator"]:
                if message.reply_to_message:
                    try:
                        unbans = message.reply_to_message.from_user.id
                        bot.unban_chat_member(message.chat.id, unbans)
                        bot.reply_to(message, unban_msg)
                    except Exception as errkick:
                        raise Exception("bot hasn't admin rights. ERROR_523")
                else:
                    bot.reply_to(message, "Reply to message from users to unban him")
        
            else:
                bot.reply_to(message, "You're not an admin of this group")

        try:
            bot.polling(none_stop= True) # Run bot without stop
        except Exception as errpol:
            raise Exception("Bad request from telegram api. [Cannot run bot. Check your internet connection]. ERROR_400") # If can't run bot then raise error

    else:
        raise Exception("Python version error. PyGroupBot bot need python3") # If python version not satisfied for pygroupbot then show error