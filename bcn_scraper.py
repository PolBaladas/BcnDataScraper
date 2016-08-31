#-*- coding: utf-8 -*-
#bcn_scraper.py
"""
    Requirements:
    - requests (installation: pip install requests)
    - BeautifulSoup (installation: pip install beautifulsoup4)
"""
import requests
from bs4 import BeautifulSoup
import sys

def getSoup(url):
    html_data = requests.get(url).text
    soup = BeautifulSoup(html_data)
    return soup

def getRows(soup):
	rows = soup.find_all('td', class_="WhadsDades")
	return cleanRows(rows)

def cleanRows(rows):
	l = []
	for r in rows:
		l.append(r.text[:-2])
	return l

def getColumns(soup):
	columns = soup.find_all('td', class_="WhadsColVar1")
	return cleanColumns(columns)

def cleanColumns(columns):
	l = []
	for c in columns:
		l.append(c.text[:-2])
	return l

def getTitle(soup):
	pass

def getSubTitle(soup):
	pass

def cleanSoup(soup):
	return soup.find('table')

def buildDict(url):
	raw_soup = getSoup(url)
	soup = cleanSoup(raw_soup)
	d = {}
	d['tit'] = getTitle(soup)
	d['subtit'] = getSubTitle(soup)
	d['columns'] = getColumns(soup)
	d['rows'] = getRows(soup)
	d['data'] = getData(soup)

url=sys.argv[1]
d = buildDict(url)
print(d)