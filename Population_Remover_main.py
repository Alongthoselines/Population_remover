# coding=utf-8
import time
population="ACB" #Population to ignore in the out file 
list1=[]

start_time =time.time()
#We first extract ID of individuals in population
with open("labels.txt") as f:
	with open("output_pop.txt", "w") as f1:
		for line in f:
			if population in line:
				list1.append(line.split()[0])
			else:
				f1.write(line)

print("Number of {} found is {} ".format(population, len(list1)))
import pdb ; pdb.set_trace()
#Take the individuals on the list out of train.raw			
with open("train.raw") as f:
	with open("train_new.txt", "w") as f1:
		j=0
		for line in f:
			
			if line.split()[1] not in list1:
					f1.write(line)
					j=j+1
			print(j)
				
print('--- {} seconds ----'.format(time.time()-start_time))