from datetime import datetime as dt
from urllib.request import urlopen

from bs4 import BeautifulSoup


def parsing_python_org_upcoming_events():
    """Выводит анонсированные события с python.org.

    Анонсированные события размещены в блоке 'Upcoming Events'.
    Чтобы найти этот блок, проводим поиск по названию 'Upcoming Events' в
    тегах h2. Из найденного h2 переходим в родительский div и получаем
    нужный блок.
    В блоке перебираем все события в тегах li и выводим на печать события,
    месяц которых соответствует заданию.
    """
    url = 'https://www.python.org/'
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup.find_all('h2')
    for tag in tags:
        for string in tag.strings:
            if string == 'Upcoming Events':
                upcoming_events_div = tag.parent

    events_list = upcoming_events_div.find_all('li')
    for event in events_list:
        event_date = dt.fromisoformat(event.time['datetime'])
        current_month = dt.today().month
        next_month = current_month + 1 if current_month != 12 else 1
        if event_date.month in (current_month, next_month):
            yield event_date.date(), event.a.string


if __name__ == "__main__":
    for event in parsing_python_org_upcoming_events():
        print(*event)
