## find where a "true" is for missing points

import csv
import glob

files = glob.glob("./part*.csv")

for table in files:
	with open(table, "r") as file:
		lines = list(csv.reader(file))
		for i in range(len(lines)):
			if(len(lines[i])!= 0):
				if(lines[i][7] == "True"):
					print("have! ", table, "at", i+1)

# result:
# have!  .\part1.csv at 21173
# have!  .\part1.csv at 152725
# have!  .\part3.csv at 28057
# have!  .\part4.csv at 154681
# have!  .\part7.csv at 146419
# have!  .\part8.csv at 44055
# have!  .\part8.csv at 176517
# have!  .\part9.csv at 154121
# have!  .\part13.csv at 80911
# have!  .\part15.csv at 13287


