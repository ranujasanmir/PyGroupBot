import pygroupbot # Importing PyGroupBot

token = "<YOUR-TELEGRAM-BOT-TOKEN>" # Initializing Bot Token(Get it from @botfather)

start_message = "Hi I'm group manage bot" # Message you want to show when user said /start
menu_message = "Here is a my all commands" # Message you want to show when user said /menu
help_message = "Get my help" # Message you want to show when user said /help
kick_message = "User kicked from group" # Message you want to show after user kicking
ban_message = "User baned from group" # Message you want to show after user banning
unban_message = "User unbaned from group" # Message you want to show after  user unbanning


# For run bot without stoping and provide all your message text to bot.
pygroupbot.online(start_message, menu_message, help_message, kick_message, ban_message, unban_message, token)


# You have to follow this example. You have to provide all message text a-z. If not bot will not run.
# Created by Ranuja Sanmira, PixCap TM.
# This library is not opensource!