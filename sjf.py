# SJF
import heapq as hq
# number of process
SIZE=4

def sjfNonpremetive(arr):
	index = 0
	for i in range(SIZE - 1):
		index = i
		for j in range(i + 1, SIZE) :
			if (arr[j][1] < arr[index][1]) :
				index = j
			
		arr[i], arr[index]=arr[index],arr[i]
	

	# ctime stores the current run time
	ctime = arr[0][1]

	
	wait=[]

	temp = arr[0][1]

	
	hq.heappush(wait,arr[0].copy())
	arr[0][1] = -1

	print("Pid",end="\t\t")
	print("AT",end="\t\t")
	print("BT",end="\t\t")

	print()

	while (wait) :

		#print(end="\t")
		print(wait[0][2],end= "\t\t")
		print(wait[0][1],end="\t\t")
		print(wait[0][0],end="\t\t")
		print()


		ctime += wait[0][0]

		
		hq.heappop(wait)

		for i in range(SIZE):
			if (arr[i][1] <= ctime
				and arr[i][1] != -1) :
				hq.heappush(wait,arr[i].copy())
				arr[i][1] = -1
			

# Driver Code
if __name__ == '__main__':
	arr=[None]*SIZE

	arr[0] =[3, 4, "p1"]
	arr[1] = [8, 0, "p2"] 
	arr[2] = [4, 5, "p3"] 
	arr[3] = [2, 9, "p4"] 

	print("Process scheduling according to SJF is: \n")

	sjfNonpremetive(arr)





