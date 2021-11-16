import re
import json
import requests
import urllib 
import argparse
import glob 
import parse
from parse import search
import csv
import datetime

#if __name__ == "__main__":
    
parser = argparse.ArgumentParser()
parser.add_argument("--input", dest="input", default="listing.txt")
parser.add_argument("--output", dest="output", default="vaudeville_dictionary.json")
args = parser.parse_args()
dated_dictionary = {}
dated_list = []
  #pulling in a list of towns  
with open('/home/sam/my_project/vaudeville/town_list.txt', 'r') as town_input:
        towns = town_input.read()
        towns = towns.split('\n')
        towns = towns[0:100]
        towns =  "|".join(towns)
        towns = towns.rstrip('|')

       #pulling in a list of downloaded files 
#for name in glob.glob('/home/sam/my_project/vaudeville/variety_downloads/just_txt/truly_txt/variety*'):
 #       pattern = "([0-9]{4})-([0-9]{2})"
  #      date_for_dict = re.search(pattern , name) 
   #     year  = date_for_dict.group(1)
    #    month = date_for_dict.group(2)
     #   date_tuple = (year+month)
        #date = int(date_tuple)
        date = 191201
        with open('/home/sam/my_project/vaudeville/variety_downloads/just_txt/truly_txt/variety27-1912-08_djvu.txt', 'r') as text_file:
                performance_dictionary = {}
                pattern = r"""(?P<venue>[\dA-Z]{2}[A-Z ]+)(?P<performers>[\w\W]*?)(?=[\dA-Z]{2})"""
                townpattern = fr"({towns})(([\s\S]+?)(?={towns}))"
                onboard_text = text_file.read()
                #split the onboard text into non-overlapping segments between town names 
                match = re.findall(townpattern,onboard_text)
                for example in match:
                        theater = re.finditer(pattern,example[1])
                        truth = re.search(pattern,example[1])
                        listings = {}
                        if truth:
                                for event in theater:
                                        performers_preprocess = event.group(2).split('\n')
                                        performers = []
                                        venue_name = event.group(1)
                                        kickout = False 
                                        for x in performers_preprocess:
                                                if x != '':
                                                        if len(x) < 25: 
                                                                performers.append(x)
                                                        else:
                                                                kickout = True
                                        if len(performers) < 25 and len(performers) > 3:
                                                if kickout == False: 
                                                        listings[venue_name] = performers 
                                if len(listings) > 0:        
                                        performance_dictionary[example[0]] = listings
                                       
                dated_dictionary[date] = performance_dictionary

print(dated_dictionary)
                
with open('Vaudeville_Tour_Listings_Defense_practice.txt', 'w') as out_file:
        out_file.write(json.dumps(dated_dictionary))




#with open('Vaudeville_Tour_listings_list.txt', 'w') as out_file:
 #       out_file.write(dated_list)
                       # for entry in output_list:
        #        print('TOWN NAME: ' + entry[0])
        #       print('-----------')
          #      for x in entry[1]:
           #             print(x)
            #            print('-----------')
                
        #print(performance_dictionary)


        # for text in onboard_text:
        #    if re.search(pattern,text):
         #       match =  re.finditer(pattern,text)
          #      output_structure = individual.groupdict()
       # print(output_list)
#print(output_structure)


# for match in re.finditer(pattern, text, flags=re.VERBOSE|re.UNICODE):                                                                                                                     
                #    print(match.groupdict())

#with open("vaudeville_dictionary.json", "wt") as outfile: #   json.dump(output_structure, outfile)
