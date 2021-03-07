import requests
from bs4 import BeautifulSoup
import pandas as pd


def kazan():
    res = requests.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D1%81%D1%82%D0%B0%D0%BD%D1%86%D0%B8%D0%B9_%D0%9A%D0%B0%D0%B7%D0%B0%D0%BD%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%BC%D0%B5%D1%82%D1%80%D0%BE%D0%BF%D0%BE%D0%BB%D0%B8%D1%82%D0%B5%D0%BD%D0%B0")
    soup = BeautifulSoup(res.text)

    html_of_lines = soup.find_all('table')[1].find_all('tr')

    lines = []

    for tr in html_of_lines[32:]:
        lines.append(tr.find('td').text.replace("\n", ""))

    from_s = []
    to_s = []
    for index, line in enumerate(lines[0:len(lines) - 1]):
        from_s.append(line)
        to_s.append(lines[index + 1])

    df = pd.DataFrame()
    df['Start'] = from_s
    df['End'] = to_s

    df.to_csv("out_kazan.csv")

    print(df.head())


if __name__ == "__main__":

    kazan()
    raise Exception
    res = requests.get("https://ru.wikipedia.org/wiki/%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%D1%81%D0%BA%D0%B8%D0%B9_%D0%BC%D0%B5%D1%82%D1%80%D0%BE%D0%BF%D0%BE%D0%BB%D0%B8%D1%82%D0%B5%D0%BD#%D0%9B%D0%B8%D0%BD%D0%B8%D0%B8")

    soup = BeautifulSoup(res.text)

    html_of_lines = soup.find('table', {'class': 'wikitable sortable'})

    all_lines = html_of_lines.find('tbody').find_all('tr')

    list_of_lines = []

    d = dict()

    for line in all_lines[1:len(all_lines) - 1]:
        a = line.find('a')
        l = a['title']
        l = l.replace(" ", "_")
        d[l.replace("_линия", "")] = f"https://ru.wikipedia.org/wiki/{l}"
        list_of_lines.append(l.replace("_линия", ""))

    print(d)
    print(list_of_lines)

    for key in d.keys():
        res = requests.get(d.get(key))
        soup = BeautifulSoup(res.text)
        table = soup.find_all('table', {'class': 'standard'})
        print(len(table))
        # print(table.find_all('td')[1])
        raise Exception
