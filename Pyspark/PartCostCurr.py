##This pySpark program takes input of 3 files AdditionalInfo, PartsCost and PartNumber
##Cleanses, Standardises the data and then joins the two file sets to give an end report

##imports
import csv
from io import StringIO
from operator import itemgetter
from itertools import groupby
from pyspark import SparkConf, SparkContext

dict_add = {}

#Splits the line into list
def split(line):
    reader = csv.reader(StringIO(line))
    return reader.next()

def parse_ai(line):
    if line[2] == '':
        line[2] = 'GBP' #defaulting it to 'GBP'
    return line[0],line[2]

def parse_pc(line):
    if line[6] == '':
        line[6] = dict_add[line[0]]
    return line[0], line[1],line[5],line[6]

#Group by keys and return the first row in the group
def unique_pc(line):
    for key, group in groupby(line, itemgetter(1)):
        return (list(group)[0])

def flatten(line):
    return (line[0],line[1][0],line[1][1][2],line[1][1][3])

def main(sc):
  	#Read additional_info file and parse it 
    ai_lines = sc.textFile("additional_info.csv").map(split).map(parse_ai).collect()
    #build a dictionary from additiona_info - use set function to remove duplicates
	  dict_add = dict(set(tuple(row) for row in ai_lines))
    #broadcast the dictionary on cluster
	  ai_lookup = sc.broadcast(dict_add)

    #Read PartsCost file and parse it
	  pc_lines = sc.textFile("PartsCost.csv").map(split).map(parse_pc)
    #read the second column as key for grouping
	  map_pc = pc_lines.map(lambda x: (x[1], x))
	  #Reduce by key and return first row per key
    red_pc = map_pc.reduceByKey(unique_pc)
    red = red_pc.map(lambda x: x[1]).collect()
	
	  #Read PartNumber file and parse it
    pn_lines = sc.textFile("PartNumber.csv").map(split).collect()
	  #Remove the duplicates by using set function
    un_pn = sc.parallelize(set(tuple(row) for row in pn_lines))
    #join PartNumber and PartCost 
	  pc_pn = un_pn.join(red_pc)

	  #Return the required columns as output
    result = pc_pn.map(flatten)

if __name__ == "__main__":
    conf = SparkConf().setMaster("local[*]")
    conf = conf.AppName("PART COST REPORT")
    sc = SparkContext(conf = conf)

    main(sc)
