# coding=utf-8
population="ACB" #Population to ignore in the out file 
i=0
#We first extract ID of individuals in population
with open("labels.txt") as f:
	with open("output_pop.txt", "w") as f1:
		f1.writelines(f.readlines())
		next(f) #Skip header line
		for line in f:
			if population in line:
				list1.append(line.split(" ")[0])
				i=i+1 #Keep track of the number of target individuals
			else:
				f1.write(line)

print("Number of %s found is %i ",format(population, i))

#Take the individuals on the list out of train.raw			
with open("output_pop.txt") as f:
	with open("train_new.txt", "w") as f1:

		for line in f:
			for iteration in range(len(list1)):
				if list1[iteration] in line:
					f1.write(line)