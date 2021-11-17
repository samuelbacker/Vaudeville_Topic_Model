import json 
import argparse
import re 

parser = argparse.ArgumentParser()
parser.add_argument("--input", dest= "input", help="input file" )
parser.add_argument("--output_file", dest="output_file", help="output file")
args = parser.parse_args()
file_input = args.input
output_file = args.output_file
noise_list = ["2d half","(ubo)","(ubo)  ","(ubo)    ","(orph) ","B. F. Keith's ","2d balf ","2d halt " ,"(One to All) ","(One to nil) ","(Inter) ","(Others to fill) ","2d half ","Hippodrome ",'i ','1 ','m ','I ','• ','* ','Sunday Opening) ','\\ ','8 ','H ','(C) ','3 ','(Sunday opening) ','(inter) ','(aAh)','Co ',': ','a ','Pantages ','(One to ','(craw) ',') ','^ ','O ','s ','R ','W ','T ','t ','2d bait ','(p) ','" ',', N. Y. ','2 ','(fox) ','B ','X ','Mc','/ ','(Two to ','! ','$',"(Three to fill) ", "(loew)", "(One to fill) ", "(wva) ","S (ubo)", "(Two to fill) ","(m) ", ". ","1st half ", '(Open Sun Mat)'] 
                
caught_count = 0

with open(file_input, 'r') as input_file:
    data = input_file.read()
    org_dict = json.loads(data)
    x = org_dict.keys()
    flat_dictionary_list = []
    for date in x:
        calendar_date = date 
        cities  = org_dict[date]
        y = cities.keys()
        for city in y:
            city_name = city 
            venues = cities[city]
            venue_list = venues.keys()
            for venue in venue_list:
                venue_name = venue
                performers = venues[venue]
                for name in performers:
                       for noise in noise_list:
                        if name == noise:
                            performers.remove(noise)
                            caught_count = caught_count + 1
                for name in performers:            
                    if '(' or ')'  in name:
                        performers.remove(name)
                        caught_count = caught_count + 1
                performer  = { "date" : date, "city_name" : city, "venue_name" : venue, "artist" : performers}
                fuss_date = performer["date"]
                pattern = "([0-9]{4})([0-9]{2})"
                if re.search(pattern, fuss_date): 
                    fuss_date = int(fuss_date)
                    if 191000 < fuss_date < 192000 :
                        flat_dictionary_list.append(performer)
print(caught_count)


with open (output_file, 'w') as out_file:
    out_file.write(json.dumps(flat_dictionary_list))
          

        #for x in output_list:
         #   print("The date is:" + x[0])
          #  for y in x[1]:
           #     print("The city is:" +  x[1[0]])
            #    for z in x[1[1]]:
             #       print("The venue is:"+  x[1[1[0]]])
              #      print("The performers are:")
               #     for a in x[1[1[1]]]:
                 #       print(a)
                        
