import requests
from bs4 import BeautifulSoup


def get_clear_list(s):
    clear_list = []
    for string in s:
        if '(' not in string and ')' not in string and string != '\n':
            clear_list.append(string)
    return clear_list


if __name__ == "__main__":
    r = requests.get('https://infotables.ru/strany-i-goroda/1066-metro-moskvy-spisok-stantsij')

    soup = BeautifulSoup(r.text)

    # all tables
    table = soup.find_all('table')[1]

    all_tr = table.find_all('tr')

    for i in range(1, len(all_tr)):
        html_str = all_tr[i]
        h5 = html_str.find('h5')
        if h5 is not None:
            line = h5.text.replace("Список станций метро ", "").replace("Москвы ", "")
        else:
            tds = html_str.find_all('td')
            list_of_stations = tds[1].get_text(separator=" ").split(" ")

            station_str = ""
            stations = []

            clear_list_of_stations = get_clear_list(list_of_stations)

            for index, station in enumerate(clear_list_of_stations):

                if index == len(clear_list_of_stations) - 1:
                    station_str += station
                    stations.append(station_str)
                    station_str = ""

                if station == '':
                    stations.append(station_str)
                    station_str = ""
                else:
                    station_str += station + " "

            print(stations)
