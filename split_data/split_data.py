import csv

with open("train.csv", "r") as file:
	lines = list(csv.reader(file))
	i = 0
	batches = int(len(lines) / 18)
	for offset in range(0, len(lines), batches):
		end = offset + batches
		if end > len(lines):
			end = len(lines)
		filename = "part" + str(i) + ".csv"
		with open(filename, "w") as newfile:
			if offset != 0:
				csv.writer(newfile).writerow(lines[0])
			for j in range(offset, end):
				csv.writer(newfile).writerow(lines[j])
		i += 1