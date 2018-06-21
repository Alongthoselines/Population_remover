# coding=utf-8
#extraire individus membre de ACD
open("out1.txt", "w").writelines([l for l in open("in.txt").readlines() if "ACB" in l])

#créer nouveau fichier en copiant les individus non-identifiés dans la première étape
list1=[]
with open("out1.txt") as f:
	for line in f:
		list1.append(line.split(" ")[0])
print(list1[2])
# list1=['hihi', 'lulz','ligne']
# open("out1.txt", "w").writelines([l for l in open("in.txt").readlines() if l.split(" ")[1] in "ligne hihi lulz"]) #est case sensitive

#"2.7.0_bf4fda703454".split("_") returns this list ['2.7.0', 'bf4fda703454']

with open("in.txt") as f:
	with open("out1.txt", "w") as f1:

		for line in f:
			for iteration in range(len(list1)):
				if list1[iteration] in line:
					f1.write(line)