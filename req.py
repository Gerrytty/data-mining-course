import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    # station_from = 205
    # station_to = 119
    # res = requests.get(f'https://www.moscowmap.ru/metro.html#m{station_from}m{station_to}')
    res = requests.get('https://www.moscowmap.ru/metro.html#lines')

    # f = open("test.html", 'w')
    # f.write(res.text)
    # f.close()

    soup = BeautifulSoup(res.text)

    list_of = soup.find_all('div', {'class': 'js-metro-stations t-metrostation-list-table'})

    for lines in list_of:
        all_p = lines.find_all('p')
        for p in all_p:
            spans = p.find_all('span')
            station_name = spans[1].text
            print(station_name)
            if len(spans) > 2:
                title_of_transition = spans[2]['title']
                print(title_of_transition)

        print("\n\n")