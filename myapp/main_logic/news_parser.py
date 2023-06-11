import feedparser

def get_news(url):
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