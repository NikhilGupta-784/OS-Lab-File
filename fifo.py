# FIFO page replacement 

from queue import Queue 

def pageFaults(pages, n, capacity): 
	
	s = set() 
	indexes = Queue() 
	page_faults = 0

	for i in range(n): 
		
		# Check if the set can hold 
		# more pages 
		if (len(s) < capacity): 
			
			if (pages[i] not in s): 
				s.add(pages[i]) 

				# increment page fault 
				page_faults += 1

				# Push the current page into the queue 
				indexes.put(pages[i]) 

		# If the set is full then need to perform FIFO 
		# i.e. remove the first page of the queue from 
		# set and queue both and insert the current page 
		else: 
			
			# Check if current page is not 
			# already present in the set 
			if (pages[i] not in s): 
				
				# Pop the first page from the queue 
				val = indexes.queue[0] 

				indexes.get() 

				# Remove the indexes page 
				s.remove(val) 

				# insert the current page 
				s.add(pages[i]) 

				# push the current page into the queue 
				indexes.put(pages[i]) 
				page_faults += 1

	return page_faults 

# Driver code 
if __name__ == '__main__': 
	pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2] 
	n = len(pages) 
	capacity = 4
	print("Total page faults: ", pageFaults(pages, n, capacity)) 

