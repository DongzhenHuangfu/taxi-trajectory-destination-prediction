## find where a "true" is for missing points

import csv
import glob
import numpy as np

files = glob.glob("./part*.csv")

def str2array(string):

	string_copy = string

	together = ''

	for i in string_copy:
		if(i != '['):
			together += i

	first = together.split("],")

	ret = []

	for i in range(len(first)):
		if(i==len(first)-1):
			second = ''
			for j in first[i]:
				if(j!=']'):
					second += j
			second = second.split(",")
		else:
			second = first[i].split(",")
		ret.append([float(second[0]), float(second[1])])
	return ret

for table in files:
	with open(table, "r") as file:
		lines = list(csv.reader(file))
		number = str2array(lines[2][8])
		print(number[0][0])
		print(number[0][0]+1)
		print()
