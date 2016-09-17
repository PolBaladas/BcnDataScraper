#-*- coding: utf-8 -*-
# bcn_scraper.py
"""
    Requirements:
    - requests (installation: pip install requests)
    - BeautifulSoup (installation: pip install beautifulsoup4)
"""
import requests
from bs4 import BeautifulSoup
import sys
import json


def makeSoup(url):
    html_data = requests.get(url).text
    soup = BeautifulSoup(html_data)
    return soup


def getTitle(soup):
    return soup.find_all('td', class_="WhadsTitVar1"
                         )[0].text.encode('ascii', 'ignore')


def getSubTitle(soup):
    return soup.find_all('td', class_="WhadsTitVar2"
                         )[0].text.encode('ascii', 'ignore')


def getRowsNames(soup):
    rows = soup.select('td[class*="WhadsRowVar"]')
    return cleanTags(rows)


def getColumnsNames(soup):
    cols = soup.select('td[class*="WhadsColVar"]')
    return cleanTags(cols)


def getData(soup):
    data = []
    dataRows = soup.find_all('tr')
    for d in dataRows:
        dataRow = d.find_all('td', class_="WhadsDades")
        cleanDataRow = cleanDataRows(dataRow)
        if cleanDataRow:
            data.append(cleanDataRow)
    return data


def cleanSoup(soup):
    return soup.find('table')


def cleanTags(tags):
    l = []
    for t in tags:
        l.append(t.text.encode('ascii', 'ignore'))
    return l


def cleanDataRows(data):
    l = []
    for d in data:
        d_clean = d.text[:-2]
        if d_clean != '':
            l.append(d_clean)
    if l:
        return l
    else:
        return False


def buildDict(url):
    raw_soup = makeSoup(url)
    soup = cleanSoup(raw_soup)
    d = {}
    d['url'] = url
    d['tit'] = getTitle(soup)
    d['subtit'] = getSubTitle(soup)

    cols = getColumnsNames(soup)
    d['cols'] = cols[1:]
    d['rows_title'] = cols[0]

    rows = getRowsNames(soup)
    d['rows'] = rows

    data = getData(soup)
    d['data'] = {}

    for c in cols[1:]:
        d['data'][c] = {}
        for r in rows:
            try:
                value = data[rows.index(r)][(cols[1:]).index(c)]
                d['data'][c][r] = value
            except:
                pass
    return d

url = sys.argv[1]
taula = buildDict(url)
json_taula = json.dumps(taula, sort_keys=True,
                        indent=4, separators=(',', ':'))

print(json_taula)
