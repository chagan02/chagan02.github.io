import csv
import json
import os
import time

# Set working Directory
global workingdir
workingdir = os.path.dirname(os.path.realpath(__file__))
workingdir = '/'.join(workingdir.split('\\')) + '/'

#Get WFO
WFO = raw_input("Enter Your WFO 3 Letter ID (example: MRX): ")
WFO = WFO.upper()

#Get List of Files
filelist = os.listdir(workingdir)
#print str(filelist)

#Create JSON File
jsonfile = open('VLJSON.json', 'w')
jsonfile = open('VLJSON.json', 'a')
jsonfile.write('{\n"rows":[\n')

#Read in CSVs and Dump to JSON
print "Dumping to JSON for " + str(WFO)
fieldnames = ("NAME","ADDRESS","PHONE","CITY","COUNTY","STATE","LAT","LON","TYPE","WFO")
for filename in filelist:
        print "Reading in " +  str(filename)
        if ".csv" in filename:
                csvfile = open(workingdir + filename, 'r')
                reader = csv.DictReader(csvfile, fieldnames)
                next(reader, None)
                for row in reader:
                        #print str(row["WFO"]) + ' ' + str(WFO)
                        if row["WFO"] == str(WFO):
                                json.dump(row, jsonfile,sort_keys=True)
                                jsonfile.write(',\n')
                                
#Remove CRLF and last comma
jsonfile.seek(-3, os.SEEK_END)
jsonfile.truncate()

#Continue
jsonfile.write('\n}]\n}')
jsonfile.close()
print "JSON Complete"
time.sleep(3)
