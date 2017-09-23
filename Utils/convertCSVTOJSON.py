import csv
import json
import sys
def convertCSVtoJSON(csvfile):

    fieldnames = ('Sr.NO','State','Till March 2016','March-2016 till jan 2017','Till Jan 2017')
    reader = csv.DictReader(csvfile, fieldnames)
    reader.next()

    # jsonFile = open('../Data/temp/out.json','w')
    data=[]
    for row in reader:
        data.append(row)
    return json.dumps(data)

if __name__=='__main__':
    csvfile = open(sys.argv[1], 'r')
    jsonData = convertCSVtoJSON(csvfile)
