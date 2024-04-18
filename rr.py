# RR

def findWaitingTime(processes, n, bt, wt, quantum): 
	rem_bt = [0] * n

	# Copy the burst time into rt[] 
	for i in range(n): 
		rem_bt[i] = bt[i]
	t = 0 # Current time 

	
	while(1):
		done = True
		for i in range(n):
			
			# If b>0 
			if (rem_bt[i] > 0) :
				done = False # There is a pending process
				
				if (rem_bt[i] > quantum):

					# how much time a process has been processed 
					t += quantum 

					# Decrease the burst_time of current process by quantum 
					rem_bt[i] -= quantum 
				
				# If burst time <= quantum
				else:
				
					# how much time a process has been processed 
					t = t + rem_bt[i] 

					# WT = current time - time used by this process 
					wt[i] = t - bt[i] 

					# process gets fully executed 
					rem_bt[i] = 0
				
		# If all processes are done 
		if (done == True):
			break
			
def findTurnAroundTime(processes, n, bt, wt, tat):
	
	# Calculating turnaround time 
	for i in range(n):
		tat[i] = bt[i] + wt[i] 


def findavgTime(processes, n, bt, quantum): 
	wt = [0] * n
	tat = [0] * n 

	findWaitingTime(processes, n, bt, wt, quantum) 
 
	findTurnAroundTime(processes, n, bt, wt, tat) 

	# Display processes along with all details 
	print("Pid \t\t BT \t\t WT \t\t TAT")
	total_wt = 0
	total_tat = 0
	for i in range(n):

		total_wt = total_wt + wt[i] 
		total_tat = total_tat + tat[i] 
		print(" ", i + 1, "\t\t", bt[i], "\t\t", wt[i], "\t\t", tat[i])

	print("\nAverage waiting time = %.5f "%(total_wt /n) )
	print("Average turn around time = %.5f "% (total_tat / n)) 
	
# Driver code 
if __name__ =="__main__":
	
	# Process id's 
	proc = [1, 2, 3]
	n = 3

	# Burst time of all processes 
	burst_time = [10, 5, 8] 

	# Time quantum 
	quantum = 2; 
	findavgTime(proc, n, burst_time, quantum)