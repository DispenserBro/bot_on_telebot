# TeleBot test bot 

## General information

<details><summary>Currently this bot has these features:</summary>
<p>

- [x] Send weather forecast for 3 days as image
- [x] Send weather forecast for the week as text
- [x] Send layered menu to user (only in private chat)
- [x] React on `А.` and `а.` ending phrases (cyrrilic, only in groups)
- [x] Mute group members
- [x] Ban and unban members

</p>
</details>

### Setting up the bot

To set up a bot, you first need to clone this repository

Then create python virtual environment besides "bot_app" directory via `python -m venv env`,

install all dependencies via `pip install -r requirements.txt`

Then paste your bot token received from [@BotFather](https://t.me/BotFather) into [config_example.yaml](./bot_app/config_example.yaml) and rename it into "config.yaml"

Finally, do `cd bot_app` and `python main.py`

*That's all!*

### Usage


All bot commands will be shown with the following commands:
`/start`
`/help`

<!-- 
```Shell
cd ed
``` 
-->
