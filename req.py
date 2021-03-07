import requests
from bs4 import BeautifulSoup
import regex as re
import pymorphy2


class Station:

    def __init__(self, name, color_of_station, list_of_transitions_by_station=None):
        self.name = name
        self.transition = list_of_transitions_by_station
        self.color_of_station = color_of_station


def has_transition(arr_spans):
    return len(arr_spans) > 2


def get_html_by_two_stations(station_from, station_to):
    return requests.get(f'https://www.moscowmap.ru/metro.html#m{station_from}m{station_to}').text


def get_dict_of_lines(soup):
    all_lines = soup.find_all('div', {'class': ['js-toggle-depend', 's-depend-control-single', 's-depend-is-init',
                                                's-depend-control-active']})
    dict_of_lines = dict()

    for i, line in enumerate(all_lines):
        dict_of_lines[line.text] = i

    return dict_of_lines


def clear_transition(s, dict_of_lines):
    # Достаём название станции из кавычек
    name_of_station = re.findall('«(.*?)»', s)
    match = re.findall('[^»]*$', s)
    # Достаём название линии - всё что идёт после кавычек
    line_name = match[0][1:len(match[0])]

    # Приводим к нормальной форме
    line_name = get_normal_form(line_name)

    if line_name == "мцк":
        line_name = "центральное кольцо"

    return Station(name_of_station, f'ln-{dict_of_lines.get(line_name) + 1}')


def get_normal_form(s):
    s = s.lower()
    morph = pymorphy2.MorphAnalyzer()
    normal_form = morph.parse(s)[0].normal_form

    return normal_form


if __name__ == "__main__":

    # clear_transition('кольцевой линии', 0)

    res = requests.get('https://www.moscowmap.ru/metro.html#lines')

    soup = BeautifulSoup(res.text)

    html_of_lines = soup.find_all('div', {'class': 'js-metro-stations t-metrostation-list-table'})

    # print(html_of_lines)

    dict_of_lines = get_dict_of_lines(soup)

    print(dict_of_lines)

    # raise Exception

    all_lines = []

    for index, lines in enumerate(html_of_lines):
        all_lines.append([])
        all_p = lines.find_all('p')
        for p in all_p:
            spans = p.find_all('span')
            station_name = spans[1].text
            list_of_transitions = []

            if has_transition(spans):
                for transition in spans[2:]:
                    title_of_transition = transition['title']
                    color = transition['class'][1]
                    # station = Station(title_of_transition, color)
                    station = clear_transition(title_of_transition.lower(), dict_of_lines)
                    list_of_transitions.append(station)

            station = Station(station_name, f'ln-{index + 1}')
            if has_transition(spans):
                station.transition = list_of_transitions
            all_lines[index].append(station)

        # print("\n")

    for line in all_lines:
        for station in line:
            print(station.name)
            if station.transition is not None:
                for transition in station.transition:
                    print(transition.name)
        print("\n")