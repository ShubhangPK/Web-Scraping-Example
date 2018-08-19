from bs4 import BeautifulSoup
import requests
#import csv

for i in range(0,342):
  source = requests.get('https://www.yellowpages.ae/c/advs/abu-dhabi/garage-services-{}-1.html'.format(i)).text
#with open('garage-services.html') as html_file:
  soup = BeautifulSoup(source, 'lxml')
  #csv_file = open('cms_scrape.csv','w')
  #csv_writer = csv.writerow(['City/Landmark','P.O.Box_number','Telephone_number','Mobile_numbers','Fax_number'])
#print(soup.prettify())
  for article in soup.find_all('div', class_='addr'):
 #   print(headline)
     
     headline = article.text
     print(headline)
     print(';')
     print()
    # csv_writer.writerow([City/Landmark,P.O.Box_number,Telephone_number,Mobile_numbers,Fax_number])
  #csv_file.close()   
