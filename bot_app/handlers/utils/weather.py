import requests
from datetime import datetime
from urllib import request
from urllib.parse import quote
from urllib.error import HTTPError
from telebot import types

from starters.register_bot import bot, logger


# 1st weather source: wttr.in
def get_weather_image(city: str | list[str] = 'Йошкар-Ола') -> tuple[str]:
    if type(city) == list:
        city = ' '.join(city)
    url = f'https://wttr.in/{quote(city)}_pqM_lang=ru.png'
    resource = request.urlopen(url)
    filename = "./imgs/img.png"
    out = open(filename, 'wb')
    out.write(resource.read())
    out.close()
    return filename, city


def w2_geolocation(city='Йошкар-Ола'):
    pass


def send_weather_image(message: types.Message) -> None:
    logger.info("weather_info_1 triggered")

    msg_text = message.text.split()

    match msg_text:
        case [command]:
            image_file, city = get_weather_image()
        case command, *city:
            try:
                image_file, city = get_weather_image(city=city)
            except Exception as e:
                logger.error(e)
                if str(e).startswith('HTTP Error 503'):
                    bot.reply_to(message, '*Сервис недоступен*', parse_mode='MarkdownV2')
                    return
                bot.reply_to(message, '*Город введен неправильно*', parse_mode='MarkdownV2')
                return
        case _:
            bot.reply_to(message, 'Ты тупой?')
            return

    out = open(f"{image_file}", 'rb')
    bot.send_photo(
        chat_id=message.chat.id,
        photo=out,
        caption=f'Погода в городе <u><b>{city.title()}</b></u>',
        parse_mode='html',
        reply_to_message_id=message.id
    )


# 2nd weather source: open-meteo.com
def get_w2_geolocation(city: str = 'Йошкар-Ола') -> tuple:
    response = requests.get(
        f'https://geocoding-api.open-meteo.com/v1/search?name={quote(city)}&language=ru'
    )
    response = response.json()
    response = (
        round(response['results'][0]['latitude'], 4),
        round(response['results'][0]['longitude'], 4)
    )
    return response


def get_weekdays(dates: list | tuple) -> tuple:
    list_weekdays_ru = ['Воскресенье', 'Понедельник',
                        'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
    dates_tmp = [datetime.strptime(date, '%Y-%m-%d') for date in dates]
    weekdays = tuple(
        list_weekdays_ru[datetime.isoweekday(date) % 7] for date in dates_tmp
    )
    dates = tuple(
        f'{el.split("-")[2]}.{el.split("-")[1]}' for el in dates
    )
    return tuple(f'<b>{" ".join(el)}</b>' for el in zip(dates, weekdays))


def get_weather_status(weather_codes: list) -> tuple:
    weather_codes_dict = {
        (0, ): '&#9728; Ясно',
        (1, 2, 3): '&#9925; Облачно',
        (45, 48): '&#127787; Туман',
        (51, 53, 55, 56, 57): '&#9748; Морось',
        (61, 63, 65, 80, 81, 82): '&#127783; Дождь',
        (66, 67, 71, 73, 75, 77, 85, 86): '&#127784; Снег',
        (95, 96, 99): '&#9928; Гроза',
    }

    keys = []

    for el in weather_codes:
        for status in weather_codes_dict.keys():
            if el in status:
                keys.append(status)

    weather_status = tuple(
        weather_codes_dict[el] if el in weather_codes_dict else '&#10067; Неизвестно' for el in keys
    )
    return weather_status


def get_temp_formats(min_temps: list | tuple, max_temps: list | tuple) -> tuple:
    min_temps = tuple(f'Мин. температура: {el} °C' for el in min_temps)
    max_temps = tuple(f'Макс.температура: {el} °C' for el in max_temps)
    return min_temps, max_temps


def get_w2_forecast(city: str | list[str] = 'Йошкар-Ола') -> tuple:
    if type(city) == list:
        city = ' '.join(city)

    lat, lon = get_w2_geolocation(city)

    response = requests.get(
        f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone=Europe%2FMoscow'
    )

    response = response.json()

    weekdays = get_weekdays(response['daily']['time'])
    codes = get_weather_status(response['daily']['weathercode'])
    temps_min, temps_max = get_temp_formats(
        response['daily']['temperature_2m_min'], response['daily']['temperature_2m_max']
    )

    forecast = tuple(zip(weekdays, codes, temps_min, temps_max))

    return forecast


def send_w2_info(message: types.Message):
    logger.info("weather_info_2 triggered")
    city = ''
    msg_text = message.text.split()

    match msg_text:
        case [command]:
            forecast = get_w2_forecast()
        case command, *city:
            try:
                forecast = get_w2_forecast(city)
            except Exception as e:
                logger.error(e)
                if str(e).startswith('HTTP Error 503'):
                    bot.reply_to(message, '*Сервис недоступен*', parse_mode='MarkdownV2')
                    return
                bot.reply_to(message, '*Город введен неправильно*', parse_mode='MarkdownV2')
                return
        case _:
            bot.reply_to(message, 'Ты тупой?')
            return

    if not city:
        city = 'Погода в городе <u><b>Йошкар-Ола</b></u>'
    else:
        city = f'Погода в городе <u><b>{" ".join(city)}</b></u>'

    forecast = tuple('\n'.join(el) for el in forecast)
    forecast = (city,) + forecast
    forecast = '\n\n'.join(forecast)

    bot.reply_to(
        message,
        text=forecast,
        parse_mode='html'
    )
