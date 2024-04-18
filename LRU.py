# memory's capacity to hold pages
size = 3  

reference_string = [1, 2, 1, 0, 3, 0, 4, 2, 4]
				
# creating a list to store the current pages in memory
pages = []

faults = 0      # page faults
hits = 0        # page hits

# iterating the reference string
for ref_page in reference_string:

    # if a ref_page already exists in pages list, remove it and append it at the end
    if ref_page in pages:
        pages.remove(ref_page)
        pages.append(ref_page)        
        hits += 1

    # if ref_page is not in the pages list
    else:
        faults +=1
        
        # check length of the pages list. If length of pages list
        # is less than memory size, append ref_page into pages list
        if(len(pages) < size):
            pages.append(ref_page)
        
        # if length of pages list is greater than or equal to memory size,
        # remove first page of pages list and append new page to pages
        else:
            pages.remove(pages[0])
            pages.append(ref_page)

	
# printing the number of page hits and page faults
print("Total number of Page Hits:", hits)
print("Total number of Page Faults:", faults)
