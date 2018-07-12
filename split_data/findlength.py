## find where a "true" is for missing points

import csv
import glob

files = glob.glob("./part*.csv")

max_length = 0
min_length = 9999999
count_max = 0
count_min = 0

max1_length = 0
min1_length = 9999999
count_max1 = 0
count_min1 = 0

max2_length = 0
min2_length = 9999999
count_max2 = 0
count_min2 = 0

max3_length = 0
min3_length = 9999999
count_max3 = 0
count_min3 = 0

for table in files:
	with open(table, "r") as file:
		lines = list(csv.reader(file))
		for i in range(1,len(lines)):
			if(len(lines[i])!= 0):
				if(lines[i][7] == "True"):
					continue
				else:
					if(len(lines[i][8]) <= min_length):
						min_length = len(lines[i][8]) 
					elif(len(lines[i][8]) <= min1_length):
						min1_length = len(lines[i][8])
					elif(len(lines[i][8]) <= min2_length):
						min2_length = len(lines[i][8])
					elif(len(lines[i][8]) <= min3_length):
						min3_length = len(lines[i][8])					
																		
					if(len(lines[i][8]) >= max_length):
						max_length = len(lines[i][8])
					elif(len(lines[i][8]) >= max1_length):
						max1_length = len(lines[i][8])
					elif(len(lines[i][8]) >= max2_length):
						max2_length = len(lines[i][8])	
					elif(len(lines[i][8]) >= max3_length):
						max3_length = len(lines[i][8])

		for i in range(1,len(lines)):
			if(len(lines[i])!= 0):
				if(lines[i][7] == "True"):
					continue
				else:
					if(len(lines[i][8]) == min_length):
						count_min += 1
					if(len(lines[i][8]) <= min1_length):
						count_min1 += 1
					if(len(lines[i][8]) <= min2_length):
						count_min2 += 1
					if(len(lines[i][8]) <= min3_length):
						count_min3 += 1					
																		
					if(len(lines[i][8]) == max_length):
						count_max += 1
					if(len(lines[i][8]) >= max1_length):
						count_max1 += 1
					if(len(lines[i][8]) >= max2_length):
						count_max2 += 1
					if(len(lines[i][8]) >= max3_length):
						count_max3 += 1


print("max:", max_length)
print("min:", min_length)
print("count max:", count_max)
print("count min:", count_min)

print("max1:", max1_length)
print("min1:", min1_length)
print("count max1:", count_max1)
print("count min1:", count_min1)

print("max2:", max2_length)
print("min2:", min2_length)
print("count max2:", count_max2)
print("count min2:", count_min2)

print("max3:", max3_length)
print("min3:", min3_length)
print("count max3:", count_max3)
print("count min3:", count_min3)

# result:
# max: 84570
# min: 2
# count max: 4
# count min: 5901
# max1: 83444
# min1: 17
# count max1: 8
# count min1: 5923
# max2: 67950
# min2: 18
# count max2: 13
# count min2: 6057
# max3: 57823
# min3: 19
# count max3: 23
# count min3: 7041


