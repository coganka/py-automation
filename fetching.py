import requests

def get_news(topic, from_date, to_date, lang='en', api_key='111'):
    url  = f"https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={lang}&apiKey={api_key}"
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    res = []
    for article in articles:
        res.append(f"TITLE: {article['title']}, DESCRIPTION: {article['description']}")
    return res


def get_news_from_country(country, api_key="111"):
    url  = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}"
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    res = []
    for article in articles:
        res.append(f"TITLE: {article['title']}, DESCRIPTION: {article['description']}")
    return res


def fetch_weather(city, api_key="3a56d79b0111907904c9a942d9c08f84"):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={api_key}&units=metric"
    res = requests.get(url)
    content = res.json()
    city = content["city"]["name"]

    weathers = content['list']
    with open('data.txt', 'a') as file:
        for w in weathers:
            #print(f"City: {city}, Time: {w['dt_txt']}, Temp: {w['main']['temp']}, condition: {w['weather'][0]['main']}")
            file.write(f"City: {city}, Time: {w['dt_txt']}, Temp: {w['main']['temp']}, condition: {w['weather'][0]['main']}\n")

fetch_weather("london")