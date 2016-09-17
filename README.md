# BcnDataScraper
Web Scraper to get data from http://www.bcn.cat/estadistica/catala/index.htm 

Takes a URL adress from "BCN Estadística" as command line input and returns JSON-formatted, properly-organized and ready to process data as output.

Developed for the Research Project "The Future of Internet Research" - by Pol Baladas ⌨
@PolBaladas <https://github.com/PolBaladas>

## Set up
Install the Python packages required:
``` pip install -r requirements.txt ```

Packages: Requests, BeautifulSoup

## Running the Script
``` python bcn_scraper.py [url] ```

Where [url] represents an adress from BCN Estadística site.
Good Examples:
	Public Transport Data: <http://www.bcn.cat/estadistica/catala/dades/economia/transport/tpublic/auev01.htm>

	2015 Electoral Data: <http://www.bcn.cat/estadistica/catala/dades/telec/aut/aut15/caut1001.htm>



##BCN Scraper - JSON Out
	Scrapes a "BCN Estadistica" URL and outputs data as JSON in the following structure: 
		```
		url:'' --> url 
		title:'' --> table title
		subtit:'' --> table subtitle
		cols:[] --> List of Table Columns
		rows:[] --> List of Table Rows
		```

	Example: [out_example.js]() --> <http://www.jsoneditoronline.org/?id=c65c30927f280a2c01a24d30c4673dc8>