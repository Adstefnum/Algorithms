

def pageCount(n, p):
    start = 0
    start_counter = 0 
    end = n
    end_counter = 0 
    
    if end-1 == p:
        return 0
    
    else:
    
        while True:
        	if start != p:
        	   if start != p+1:
        	   	start += 2
        	   	start_counter += 1

        	   else:
        	   	break
        	else:
        		break

		            
        while True:
        	if end != p:
        	   if end!= p-1:
        	   	end -= 2
        	   	end_counter += 1

        	   else:
        	   	break


        	else: 
        		break
    
        
        return min(start_counter,end_counter)
    
print(pageCount(6,2))