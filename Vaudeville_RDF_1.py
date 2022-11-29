from rdflib import Graph, URIRef, BNode, Literal, Namespace 
from rdflib.namespace  import Namespace, RDF, FOAF, SH, SDO
import datetime
import argparse
import json
import uuid

parser = argparse.ArgumentParser()
parser.add_argument("--input", dest="input", default ="Regex_Defense_5_Vaudeville_Dcitionary_One_Issue_Flat_List.json")
parser.add_argument("--output", dest="output", default="my_rdf_graph")
args = parser.parse_args()
input_file = args.input
output_file = args.output

CDH = Namespace("https://cdh.jhu.edu/")

with open(input_file, 'r') as f:
    input_data = json.load(f)
    g = Graph()
    g.bind("sh", SH)
    g.bind("cdh", CDH)
    g.bind("sdo", SDO)
    #adding the definitions around performers
    for i in input_data: 
        date = Literal(i["date"])
            #datetime.datetime(1910, 4, 13)) #this will be filled in with the actual date information. 
            #Performance = URIRef("https://cdh.jhu.edu/")#namespace for event?
        venue = Literal(i["venue_name"])
        city = Literal(i["city_name"])
        performer_name = Literal(i["artist"])
        #print(performer_name)
        #print(venue)
        uid = uuid.uuid1()
        new_performer_uri = URIRef(CDH + str(uid))
        #print(new_performer_uri)
        g.add((new_performer_uri, RDF.type, SDO.Person))
        g.add((new_performer_uri, SDO.name, performer_name))
        #g.add((new_performer_uri, SDO.performer, venue))
        g.add((venue, RDF.type, SDO.EventVenue))
        g.add((venue, SDO.containedInPlace, city))
        performance = BNode()
    #adding the definitions around the event/bill
        g.add((new_performer_uri, SDO.performer, performance))
        g.add((performance, RDF.type, SDO.MusicEvent ))
        g.add((performance, SDO.startDate, date))
        g.add((performance, SDO.location, venue))
    #adding the definitions around the venue
        #g.add((venue, RDF.type, SDO.Place))
        #g.add((venue, SDO.containedInPlace, city))
    print(g.serialize(format='turtle'))
    g.serialize(destination= output_file, format='turtle')
