import requests
from datetime import datetime
from os import getenv, system
from dotenv import load_dotenv
load_dotenv()

WEATHER_API = getenv('WEATHER_API')

def WeatherService(get_city, API=WEATHER_API):
    """
    Ваш бот-метеоролог мгновенно показывает погоду в любом городе, предоставляя актуальную информацию о температуре воздуха, влажности и вероятности дождя. 
    Это помогает планировать дела эффективнее и быть в курсе погодных событий в режиме реального времени.
    
    get_city = 'Almaty'
    API = WEATHER_API

    WeatherService(get_city: str, API: StrApiKey) -> str
    """

    url = f'https://api.openweathermap.org/data/2.5/weather?q={get_city}&appid={API}&units=metric'

    response = requests.get(url)
    data = response.json()
    try:
        Pr_Day = datetime.fromtimestamp(data['sys']['sunset']) - datetime.fromtimestamp(data['sys']['sunrise'])

        Informations = f"""Погода - Marselle.naz
        Страна: {data["sys"]['country']['😀']}
        Город: {data['name']} - {data['weather'][0]['description']} {data['clouds']['all']}%
        Температура: {data['main']['temp']}°C
        Ощушается: {data['main']['feels_like']}°C
        Влажность: {data['main']['humidity']}%
        Давление воздуха: {data['main']['pressure']} гПа
        Скорость ветра: {data['wind']['speed']} м/с
        Направление ветра: {data['wind']['deg']}°
        Восход солнце: {datetime.fromtimestamp(data['sys']['sunrise'])}
        Продол-ть дня: {Pr_Day}
        Закат солнце: {datetime.fromtimestamp(data['sys']['sunset'])}
        """
        system("clear")
        return Informations
    except: 
        return "Нет такого времени!!!"