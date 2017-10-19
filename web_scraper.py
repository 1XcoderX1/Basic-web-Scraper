from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from datetime import datetime


quote_page = ['http://www.moneycontrol.com/india/stockpricequote/computers-software-medium-small/firstsourcesolutions/FS07', 'http://www.moneycontrol.com/india/stockpricequote/textiles-processing/sarlaperformancefibers/SPF01']


data = []

for pg in quote_page :
    # query the website and return the HTML version of it to page
    page = urlopen(pg)
    # parse the HTML using beautiful soup and store in variable 'soup'
    soup = BeautifulSoup(page, 'html.parser')
    print(soup)
    # take out the <div> and get its value
    name_box = soup.find('h1', attrs={'class':'b_42'})
    name = name_box.text.strip()
    # get the price
    price_box = soup.find('div', attrs={'class':'FL PR5 rD_30'})
    price = price_box.text.strip()
    # save the data in a tuple
    data.append((name, price))

    print("Succesfully Added" ,name ,"at", price, "on", datetime.now())

# write everything to an external csv file
writer = csv.writer(open('stock_indices.csv', 'w'))
for name, price in data:
    writer.writerow([name, price, datetime.now()])
