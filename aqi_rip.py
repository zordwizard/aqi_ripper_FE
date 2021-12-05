import datetime
import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd
import haversine as hs



#general variables
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36"}
heute = datetime.date.today()
zeit = datetime.datetime.now().time()
heute = str(heute)

#functions

#defining the write to csv function
def write_to_file(stuff_to_write, where_to_write):
	with open(where_to_write, 'a', encoding='UTF8') as f:
		writer = csv.writer(f)
		# write stuff
		writer.writerow(stuff_to_write)



def write_mid_file(value, index):
    file_path = "aqi_rip.py"
    index= index -1
    value =str(value) + "\n"
    print(value)


    with open(file_path, "r") as f:
        contents = f.readlines()

        contents.insert(index, value)

    with open(file_path, "w") as f:
        contents = "".join(contents)
        f.write(contents)



#example entry
#Locations
#Distances
#url
#page var
#




print("start")












#Locations
fort_erie_loc = (42.901775, -78.972176)
london_on_loc = (42.983612, -81.249725)
buffalo_ny_loc = (42.880230, -78.878738)
phoenix_az_loc = (33.448376, -112.074036)
nyc_ny_loc = (40.730610, -73.935242)
toronto_on_loc = (43.651070, -79.347015)

#Distances
london_on_dist = hs.haversine(fort_erie_loc, london_on_loc)
buffalo_ny_dist = hs.haversine(fort_erie_loc, buffalo_ny_loc)
phoenix_az_dist = hs.haversine(fort_erie_loc, phoenix_az_loc)
nyc_ny_dist = hs.haversine(fort_erie_loc, nyc_ny_loc)
toronto_on_dist = hs.haversine(fort_erie_loc, toronto_on_loc)


#web url
fort_erie_url = "https://www.accuweather.com/en/ca/fort-erie/l2a/air-quality-index/55056"
#get's the html file. the headers are crucial to avoid 403 error
fort_erie_page = requests.get(fort_erie_url, headers= headers)
#this parses the file for use
fort_erie_soup = BeautifulSoup(fort_erie_page.content, 'html.parser')
#finds and reports the correct element
fort_erie_aqi = fort_erie_soup.find(class_="aq-number").get_text()
#changes the value to an integer for easy algebra
fort_erie_aqi = int(fort_erie_aqi)

#Gets London, ON AQI
london_on_url = "https://www.accuweather.com/en/ca/london/n6b/air-quality-index/55489"
london_on_page = requests.get(london_on_url, headers= headers)
london_on_soup = BeautifulSoup(london_on_page.content, 'html.parser')
london_on_aqi = london_on_soup.find(class_="aq-number").get_text()
london_on_aqi = int(london_on_aqi)
gainesville_fl_url='https://www.accuweather.com/en/us/gainesville/32601/air-quality-index/328162'
gainesville_fl_loc=(29.651634,-82.324829)
gainesville_fl_page = requests.get(gainesville_fl_url, headers = headers)
gainesville_fl_soup=BeautifulSoup(gainesville_fl_page.content, 'html.parser')
gainesville_fl_aqi = int(gainesville_fl_soup.find(class_='aq-number').get_text())
gainesville_fl_dist = hs.haversine(fort_erie_loc,gainesville_fl_loc)
gainesville_fl_data = ['gainesville_fl', heute, gainesville_fl_aqi, gainesville_fl_dist, zeit]
write_to_file(gainesville_fl_data, 'aqi_checks.csv')



amsterdam_url='https://www.accuweather.com/en/nl/amsterdam/249758/air-quality-index/249758'
amsterdam_loc=(52.370216,4.895168)
amsterdam_page = requests.get(amsterdam_url, headers = headers)
amsterdam_soup=BeautifulSoup(amsterdam_page.content, 'html.parser')
amsterdam_aqi = int(amsterdam_soup.find(class_='aq-number').get_text())
amsterdam_dist = hs.haversine(fort_erie_loc,amsterdam_loc)
amsterdam_data = ['amsterdam', heute, amsterdam_aqi, amsterdam_dist, zeit]
write_to_file(amsterdam_data, 'aqi_checks.csv')
moscow_url='https://www.accuweather.com/en/ru/moscow/294021/air-quality-index/294021'
moscow_loc=(55.751244,37.618423)
moscow_page = requests.get(moscow_url, headers = headers)
moscow_soup=BeautifulSoup(moscow_page.content, 'html.parser')
moscow_aqi = int(moscow_soup.find(class_='aq-number').get_text())
moscow_dist = hs.haversine(fort_erie_loc,moscow_loc)
moscow_data = ['moscow', heute, moscow_aqi, moscow_dist, zeit]
write_to_file(moscow_data, 'aqi_checks.csv')

#Gets Buffalo, NY AQI
buffalo_ny_url = "https://www.accuweather.com/en/us/buffalo/14202/air-quality-index/349726"
buffalo_ny_page = requests.get(buffalo_ny_url, headers= headers)
buffalo_ny_soup = BeautifulSoup(buffalo_ny_page.content, 'html.parser')
buffalo_ny_aqi = buffalo_ny_soup.find(class_="aq-number").get_text()
buffalo_ny_aqi = int(buffalo_ny_aqi)

#Gets Phoenix, AZ AQI
phoenix_az_url = "https://www.accuweather.com/en/us/phoenix/85003/air-quality-index/346935"
phoenix_az_page = requests.get(phoenix_az_url, headers= headers)
phoenix_az_soup = BeautifulSoup(phoenix_az_page.content, 'html.parser')
phoenix_az_aqi = phoenix_az_soup.find(class_="aq-number").get_text()
phoenix_az_aqi = int(phoenix_az_aqi)

#Gets NYC, NY AQI
nyc_ny_url = "https://www.accuweather.com/en/us/new-york/10007/air-quality-index/349727"
nyc_ny_page = requests.get(nyc_ny_url, headers= headers)
nyc_ny_soup = BeautifulSoup(nyc_ny_page.content, 'html.parser')
nyc_ny_aqi = nyc_ny_soup.find(class_="aq-number").get_text()
nyc_ny_aqi = int(nyc_ny_aqi)

#Gets Toronto, ON AQI
toronto_on_url = "https://www.accuweather.com/en/ca/toronto/m5h/air-quality-index/55488"
toronto_on_page = requests.get(toronto_on_url, headers= headers)
toronto_on_soup = BeautifulSoup(toronto_on_page.content, 'html.parser')
toronto_on_aqi = toronto_on_soup.find(class_="aq-number").get_text()
toronto_on_aqi = int(toronto_on_aqi)

#Creates data lists for entry
fort_erie_data= ["Fort Erie, ON", heute, fort_erie_aqi, 0, zeit]
london_on_data= ["London, ON", heute, london_on_aqi, london_on_dist, zeit]
buffalo_ny_data = ["Buffalo, NY", heute, buffalo_ny_aqi, buffalo_ny_dist, zeit]
phoenix_az_data = ["Phoenix, AZ", heute, phoenix_az_aqi, phoenix_az_dist, zeit]
nyc_ny_data = ["NYC, NY", heute, nyc_ny_aqi, nyc_ny_dist, zeit]
toronto_on_data = ["Toronto, ON", heute, toronto_on_aqi, toronto_on_dist, zeit]

#Writes lists to csv
write_to_file(fort_erie_data, "aqi_checks.csv")
write_to_file(london_on_data, "aqi_checks.csv")
write_to_file(buffalo_ny_data, "aqi_checks.csv")
write_to_file(phoenix_az_data,"aqi_checks.csv")
write_to_file(nyc_ny_data, "aqi_checks.csv")
write_to_file(toronto_on_data, "aqi_checks.csv")

data1 = pd.read_csv("aqi_checks.csv")
print(data1)
