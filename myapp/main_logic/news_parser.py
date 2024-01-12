import feedparser
import requests
from bs4 import BeautifulSoup

def get_news(url):
    """
    Функция для получения новостей с сайта dvizhok.su.
    """
    feed = feedparser.parse(url)  # Парсим RSS-фид.
    news = []
    # Получаем новости из RSS-фида и добавляем их в список news.
    for entry in feed.entries:
        news.append({
            "title": entry.title,
            "link":entry.links[0].href,
            "image": entry.links[1].href,
            "description": entry.summary
        })
    return news

def get_news_autoparts(url):
    """
    Функция для получения новостей с сайта autoparts.webnode.page.
    """
    feed = feedparser.parse(url)  # Парсим RSS-фид.
    news = []
    # Получаем новости из RSS-фида и добавляем их в список news.
    for entry in feed.entries:
        news.append({
            "title": entry.title,
            "link":entry.link,
            "image": entry.links[1].href,
            "description": entry.summary
        })
    return news

def get_new_autoparts(url):
    """
    Функция для получения новости с сайта autoparts.webnode.page.
    """
    response = requests.get(url)
    page_content = response.content
    soup = BeautifulSoup(page_content, 'html.parser')
    box = soup.find(class_='box')
    h1 = box.find('h1')
    new = {}
    new['title'] = h1.text
    date = box.find('ins')
    new['date'] = date.text
    img = box.find('img')
    new['img'] = img.text
    spans = box.find_all('span')
    text = ''
    for span in spans:
        text += span.text + ' '

def get_new(url):
    """
    Функция для получения новости с сайта autoparts.webnode.page.
    """
    response = requests.get(url)
    page_content = response.content
    soup = BeautifulSoup(page_content, 'html.parser')
    box = soup.find(class_='fullSizeBanner')
    h1 = box.find('h1')
    new = {}
    new['title'] = h1.text
    date = box.find(class_='articleDate')
    new['date'] = date.text
    img = box.find('img')
    new['img'] = img.attrs['src']
    ps = box.find_all('p')
    text = ''
    for tag_p in ps:
        text += tag_p.text + ' '
    new['text'] = text
    return new