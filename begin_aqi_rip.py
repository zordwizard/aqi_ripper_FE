import datetime
import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd
import haversine as hs

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


adding_town = True
while adding_town ==  True:
    add_town_q = input("would you like to add a town? Y/N")
    add_town_q = str(add_town_q.upper())
    if add_town_q == "Y":
        print("Sounds good, let's answer a few questions")
        new_town_name_str= input("Enter name of town: ")
        new_town_name = new_town_name_str
        if " " in new_town_name:
            new_town_name = new_town_name.replace(" ", "_")
        if "," in new_town_name:
            new_town_name = new_town_name.replace(",", "")
        print(new_town_name)
        new_coorinate1 = (input("Enter absolute latitude: "))
        new_coorinate2 = (input("Enter absolute longitude: "))
        new_location = "(" + str(new_coorinate1) + "," + str(new_coorinate2) + ")"
        new_accuweather_url = "'"+input("Enter new url: ") + "'"
        new_data = [new_location, new_accuweather_url]
        naming_data= ["_loc", "_url"]
        tracker = 0
        for data in new_data:
            print(tracker)
            print(new_data[tracker])
            write_mid_file(new_town_name + naming_data[tracker] + "=" + data, 101)
            tracker+=1
        write_mid_file(new_town_name+"_page = requests.get("+new_town_name+"_url, headers = headers)", 103)
        write_mid_file(new_town_name+"_soup=BeautifulSoup("+new_town_name+"_page.content, 'html.parser')", 104)
        write_mid_file(new_town_name+"_aqi = int("+new_town_name+"_soup.find(class_='aq-number').get_text())", 105)
        write_mid_file(new_town_name+"_dist = hs.haversine(fort_erie_loc,"+new_town_name+"_loc)", 106)
        write_mid_file(new_town_name+"_data = ["+"'"+new_town_name+"'"+", heute, "+new_town_name+"_aqi, "+new_town_name+"_dist, zeit]", 107)
        write_mid_file("write_to_file("+new_town_name+"_data, 'aqi_checks.csv')", 108)
        write_mid_file("\n", 109)
    elif add_town_q == "N":
        print("No towns added")
        adding_town = False
    else:
        print("invalid input")

exec(open("aqi_rip.py").read())
