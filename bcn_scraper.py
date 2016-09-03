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
import json

def makeSoup(url):
    html_data = requests.get(url).text
    soup = BeautifulSoup(html_data)
    return soup

def getTitle(soup):
	return soup.find_all('td', class_="WhadsTitVar1")[0].text

def getSubTitle(soup):
	return soup.find_all('td', class_="WhadsTitVar2")[0].text

def getRowsNames(soup):
	rows = soup.find_all('td', class_="WhadsRowVar1")
	return cleanTags(rows)

def getColumnsNames(soup):
	cols = soup.find_all('td', class_="WhadsColVar1")
	return cleanTags(cols)

def cleanTags(tags):
	l = []
	for t in tags:
		l.append(t.text[:-2])
	return l

def getData(soup):
	data = []
	dataRows = soup.find_all('tr')
	for d in dataRows:
		dataRow = d.find_all('td', class_="WhadsDades")
		cleanDataRow = cleanDataRows(dataRow)
		if cleanDataRow:
			data.append(cleanDataRow)
	return data

def cleanDataRows(data):
	l = []
	for d in data:
		d_clean = d.text[:-2]
		if d_clean!='':
			l.append(d_clean)
	if l:
		return l
	else :
		return False

def cleanSoup(soup):
	return soup.find('table')

def buildDict(url):
	raw_soup = makeSoup(url)
	soup = cleanSoup(raw_soup)
	d = {}
	d['url'] = url
	d['tit'] = getTitle(soup)
	d['subtit'] = getSubTitle(soup)
	d['cols'] = getColumnsNames(soup)
	d['rows'] = getRowsNames(soup)
	d['data'] = getData(soup)
	return d

url=sys.argv[1]
taula = buildDict(url)
json_taula = json.dumps(taula, sort_keys=False, 
	indent=4, separators=(',',':'))

print(json_taula)