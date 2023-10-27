import pygroupbot # Importing PyGroupBot

pygroupbot.bot.token("<BOT_TOKEN>", parse_mode= "html") # Initializing Bot Token and parse_mode. Also you can use 'Markdown' to parse_mode

start_message = "Hi I'm group manage bot" # Message you want to show when user said /start
menu_message = "Here is a my all commands" # Message you want to show when user said /menu
help_message = "Get my help" # Message you want to show when user said /help
info_message = "This is the Group Manage bot" # Message you want to show when user said /info
kick_message = "User kicked from group" # Message you want to show after user kick
ban_message = "User banned from group" # Message you want to show after user ban
unban_message = "User unbanned from group" # Message you want to show after  user unban

# Input variables to bot
pygroupbot.start_message(start_message)
pygroupbot.menu_message(menu_message)
pygroupbot.help_message(help_message)
pygroupbot.info_message(info_message)
pygroupbot.kick_message(kick_message)
pygroupbot.ban_message(ban_message)
pygroupbot.unban_message(unban_message)

# Run bot without stoping
pygroupbot.run(True)
