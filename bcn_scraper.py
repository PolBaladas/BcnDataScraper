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
	rows = soup.find_all('td', class_="WhadsRowVar1")
	return cleanRows(rows)

def cleanRows(rows):
	l = []
	for r in rows:
		l.append(r.text[:-2])
	return l

def getColumns(soup):
	data = soup.find_all('td', class_="WhadsColVar1")
	return cleanData(data)

def cleanColumns(columns):
	l = []
	for c in columns:
		l.append(c.text[:-2])
	return l

def getData(soup):
	data = soup.find_all('td', class_="WhadsDades")
	return cleanData(data)

def cleanData(data):
	l = []
	for d in data:
		d_clean = str(d.text[:-2])
		if d_clean!='':
			l.append(d_clean)
	return l

def getTitle(soup):
	return soup.find_all('td', class_="WhadsTitVar1")[0].text

def getSubTitle(soup):
	return soup.find_all('td', class_="WhadsTitVar2")[0].text


def cleanSoup(soup):
	return soup.find('table')

def buildDict(url):
	raw_soup = getSoup(url)
	soup = cleanSoup(raw_soup)
	d = {}
	d['url'] = url
	d['tit'] = getTitle(soup)
	d['subtit'] = getSubTitle(soup)
	d['cols'] = getColumns(soup)
	d['rows'] = getRows(soup)
	d['data'] = getData(soup)
	return d

url=sys.argv[1]
d = buildDict(url)
print(d)