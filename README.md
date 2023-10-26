
![Python Version](https://img.shields.io/badge/python-3.9-blue.svg)

**_`pygroupbot` is python library that can you help to create your own simple telegram group manage bot._**

## Table of Contents

- [Installation](#installation)
- [How To Use](#how-to-use)
  - [Importing the Module](#importing-the-module)
  - [More Examples](#examples)
  - [Errors](#errors)
- [Terms And Condition](#terms-and-condition)
- [License](#license)
- [About Us](#about-us)

## Installation

To integrate `pygroupbot` into your project, you can use `pip`:

```bash
pip install pygroupbot
```

pygroupbot using pytelegrambotapi library for connect with telegram api. If it's not installed after installing pygroupbot, then install it :

```bash
pip install pytelegrambotapi
```

For use pygroupbot you have to install python 3 on your device.(Python 2 is not supported!)

## How To Use

### Importing The Module

To import pygroupbot to your projects just use `import` :

```python
import pygroupbot
```

### Examples

Normal example

```python
import pygroupbot # Importing PyGroupBot

token = "<YOUR-TELEGRAM-BOT-TOKEN>" # Initializing Bot Token(Get it from @botfather)

start_message = "Hi I'm group manage bot" # Message you want to show when user said /start
menu_message = "Here is a my all commands" # Message you want to show when user said /menu
help_message = "Get my help" # Message you want to show when user said /help
kick_message = "User kicked from group" # Message you want to show after user kick
ban_message = "User banned from group" # Message you want to show after user ban
unban_message = "User unbanned from group" # Message you want to show after  user unban

# For run bot without stoping and provide all your message text to bot.
pygroupbot.online(start_message, menu_message, help_message, kick_message, ban_message, unban_message, token)

# You have to follow this example. You have to provide all message text a-z. If not bot will not run.
# Created by Ranuja Sanmira, PixCap TM.
# This library is not open source!
```

### Errors

You will face some errors while using pygroupbot.

1. **bot hasn't admin rights. ERROR_523** - Bot hasn't admin rights. Promote your bot as admin.

2. **Bad request from telegram api. [Cannot run bot. check your internet connection]. ERROR_400** - This error saying bot has problem with connecting to the telegram api. Check your device internet connection. Or create new bot token from Bot Father and give it to the bot.

3. **Python version error. PyGroupBot bot need python3** - If you see this error you have to update your python version. pygroupbot can't run on python 2. It's very old version. All potato pc's can run python 3.2. So why are you using python2?

**This errors only showing with pygroupbot. The errors from pytelegrambotapi not here!**

## Terms And Condition

1. **Use Responsibly**: This python library is developed for only education purpose.

2. **Objects**: pygroupbot has only 7 objects (start_msg, menu_msg, help_msg, kick_msg, ban_msg, unban_msg, token). You have to provide all of them a-z.

3. **Privacy**: We do not store any details about you.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## About Us

We are PixCap TM. We are from Sri Lanka. We interest on programming and software development. pygroupbot is our first python library. We have created some computer softwares. And we are developing telegram bots. You can find Medusa bot on telegram(Username : @medusa_rs45_bot). This bot has awesome tools for interact with donghua and anime world. Check it out!

**Copyright © 2020-2023 PixCap TM.**
**All rights Reserved.**

