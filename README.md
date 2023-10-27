
![Python Version](https://img.shields.io/badge/python-3.5-blue.svg)

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

Genaral example:

```python
import pygroupbot # Importing PyGroupBot

pygroupbot.bot.token("<BOT_TOKEN>", mode= "html") # Initializing Bot Token and parse_mode. Also you can use 'Markdown' to parse_mode

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

```

**How to Bold / Italic and Create Links:**

With the `Pygroupbot v1.2.2` we initialized `parse_mode` to bot. Telegram bots has two parse_mode. First one is `Markdown`. In this parse mode you can bold text using '**' symbol and italic text using '__' like in the bellow example:

```python
pygroupbot.bot.token("<TOKEN>", mode= "Markdown")

paygroupbot.start_message("*Hello Dear!* _I am the PyGroupBot_")
```

We suggest to you use `html` as parse_mode. You can bold text with '<b></b>', italic text with '<i></i>' and create links with 'a' tag using in html like in the bellow example:

```python
pygroupbot.bot.token("<TOKEN>", mode= "html")

paygroupbot.start_message("<b>Hello Dear!</b>   <i>I am the PyGroupBot</i>   <a href='https://github.com/ranujasanmir/pygroupbot'>Go to github</a>")
```

### Errors

You will face some errors while using pygroupbot.

1. **Something Wrong. ERROR_523** - Something messing in the bot. Check bot admin rights..

2. **Bad request from telegram api. [Cannot run bot. check your internet connection]. ERROR_400** - This error saying bot has problem with connecting to the telegram api. Check your device internet connection. Or create new bot token from Bot Father and give it to the bot.

```python
pygroupbot.bot.token("<NEW_BOT_TOKEN>")
```

3. **Python version error. PyGroupBot bot need python3** - If you see this error you have to update your python version. pygroupbot can't run on python 2. It's very old version. All potato pc's can run python 3.2. So why are you using python2?

4. **.run() only need boolean value!** - It's mean you entered wrong value to run() function. run() only need True or False values.

```python
pygroupbot.run(True)
```

5. **pygroupbot token must not be a null** - This saying you didn't entered token.

6. **pygroupbot mode must not be a null** - To fix this error pass the parse_mode.

7. **PyGroupBot Server Not Started Yet - Bot is Offline...** - If bot didn't running this error will be show. Make sure to make pygroupbot.run(True). If you entered False, bot will not run.

**This errors only showing with pygroupbot. The errors from pytelegrambotapi not here!**

## Terms And Condition

1. **Use Responsibly**: This python library is developed for only education purpose.

2. **Privacy**: We do not store any details about you.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## About Us

We are PixCap TM. We are from Sri Lanka. We interest on programming and software development. pygroupbot is our first python library. We have created some computer softwares. And we are developing telegram bots. You can find Medusa bot on telegram(Username : @medusa_rs45_bot). This bot has awesome tools for interact with donghua and anime world. Check it out!

**Copyright © 2020-2023 PixCap TM.**
**All rights Reserved.**

