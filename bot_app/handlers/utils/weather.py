from telebot import types
from urllib import request
from urllib.parse import quote

from starters.register_bot import bot, logger


def get_weather_image(city: str = 'Йошкар-Ола') -> str:
    url = f'https://wttr.in/{quote(city)}_pqM_lang=ru.png'
    resource = request.urlopen(url)
    filename = "./imgs/img.png"
    out = open(filename, 'wb')
    out.write(resource.read())
    out.close()
    return filename, city

def send_weather_image(message: types.Message) -> None:
    logger.info("weather_info triggered")

    msg_text = message.text.split()

    match msg_text:
        case [command]:
            image_file, city = get_weather_image()
        case [command, city]:
            try:
                image_file, city = get_weather_image(city=city)
            except Exception:
                bot.reply_to(message, 'Город не тот')
                return
        case _:
            bot.reply_to(message, 'Ты тупой?')
            return

    out = open("./imgs/img.png", 'rb')
    bot.send_photo(
        chat_id=message.chat.id,
        photo=out,
        caption=f'Погода в городе <u><b>{city}</b></u>',
        parse_mode='html',
        reply_to_message_id=message.id
    )
