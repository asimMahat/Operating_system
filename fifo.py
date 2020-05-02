#importing  Queue func from module queue
from queue import Queue 


pages = [7,1,2, 2,1, 0, 3, 0, 
				4, 2,7, 3, 0, 3, 1,2] #you can have your own list in this
length_of_pages = len(pages) 
room_size = 2
 
def fifo_page_replacement(pages, length_of_pages, room_size): 
	
	frame = set() #to check if pages[i] in set or not

	indexes = Queue()  #queue() func is called which is under module queue

	page_faults = 0#starting from initial page
	for i in range(length_of_pages): 
		
	    # checking the room_size
		if (len(frame) < room_size): 
			
			if (pages[i] not in frame): 
				frame.add(pages[i]) 

				page_faults += 1

				indexes.put(pages[i]) 

		  
		else: 
			if (pages[i] not in frame): 
				val = indexes.queue[0] 

				indexes.get() 

			  
				frame.remove(val) #removing the indexpage

			  
				frame.add(pages[i]) #using add() func to insert the page

				  
				indexes.put(pages[i]) #using func put() to push the page

				 
				page_faults += 1 #incrementing the page fault

	return page_faults 

#defining main function to print out the output
def main():
    print("By FIFO page replacement algorithm:")
    print("The number of page_fault is " ,fifo_page_replacement(pages,length_of_pages,room_size) ,".")

#running the main function
if __name__ == '__main__': 
    main()

	
  

 