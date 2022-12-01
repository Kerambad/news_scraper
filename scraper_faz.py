from bs4 import BeautifulSoup
import requests


def main():
    html_text = requests.get('https://www.faz.net/aktuell/').text
    html_text = BeautifulSoup(html_text, 'lxml')
    articles = html_text.find_all('div', 'tsr-Base_ContentWrapperInner')
    counter = 0
    for article in articles:
        header = article.find('span', class_='tsr-Base_HeadlineText')
        body = article.find('div', class_ = 'tsr-Base_Content')
        link = article.find('a', class_= 'js-hlp-LinkSwap js-tsr-Base_ContentLink tsr-Base_ContentLink')
        if header is None:
            continue
        if body is None:
            body = '%No description%'
        else:
            body = body.text.strip()
        try:
            link = article.a['href']
        except KeyError:
            link = '%No Link%'
        except TypeError:
            link = '%No Link%'

        if body == '%No description%' and link == '%No Link%':
            continue

        header = header.text.strip()
        print(header)
        print(body)
        print(link)
        print()
        counter += 1
    print(counter)


if __name__ == '__main__':
    main()
