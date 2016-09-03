# BcnDataScraper
Scraper to get data from http://www.bcn.cat/estadistica/catala/index.htm 

##bcn_scraper.py 
	Scrapes url from BCN Estadistica containing a table to JSON format in the following structure:
		```
		url:'' --> url 
		title:'' --> table title
		subtit:'' --> table subtitle
		cols:[] --> List of Table Columns
		rows:[] --> List of Table Rows
		data:[[], [], [], ...] --> Matrix with numerical data from the table
		```