# coding=utf-8
import time
population="ACB" #Population to ignore in the out file 
i=0
list1=[]

start_time =time.time()
#We first extract ID of individuals in population
with open("labels.txt") as f:
	with open("output_pop.txt", "w") as f1:
		f1.writelines("")
		#next(f) #Skip header line
		for line in f:
			if population in line:
				list1.append(line.split(" ")[0])
				i=i+1 #Keep track of the number of target individuals
			else:
				f1.write(line)

print("Number of {} found is {} ".format(population, i))

#Take the individuals on the list out of train.raw			
with open("train.raw") as f:
	with open("train_new.txt", "w") as f1:
		j=0
		for line in f:
			i=0
			j=j+1
			for iteration in range(len(list1)):
				if line.split(" ")[0] !=list1[iteration]:
					i=i+1
			print(j)
			print(i)
			print(len(list1))
			if i==len(list1):
				f1.write(line)
print('--- {} seconds ----'.format(time.time()-start_time))