from bs4 import BeautifulSoup
import requests


WEB_SOURCE = "http://web.mta.info/nyct/facts/ridership/ridership_sub_annual.htm"


def get_table(src, id):
    res = requests.get(src)
    soup = BeautifulSoup(res.text)
    return soup


def parse_row(row, borough):
    cells = row.find_all('td')
    return {
        'station_name': '', #td.div.string
        'train_lines': [line_from_image_str(i.img) for i in tr.th[0].span],
        'ridership': {

        },
        'aggregates': {

        },
        'borough': borough
    }

tree = get_table(WEB_SOURCE, 'subway')
print(tree)
import pdb; pdb.set_trace()
