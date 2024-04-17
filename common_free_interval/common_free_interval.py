import heapq
def employee_free_time(emp): 
 heap = []

 for i in range(len(emp)):
    heapq.heappush(heap,(emp[i][0][0],i,0))
 print(heap)
 prev_interval = heap[0][0]    
 print(heap,prev_interval)
 result_list = []
 # j = 1
 while heap:
    _, ID , j = heapq.heappop(heap)
    current = emp[ID][j] 
    if current[0] > prev_interval: 
          result_list.append([prev_interval,current[0]])
  
    prev_interval = max(prev_interval,current[1])
   
    if  j+1 < len(emp[ID]):
      heapq.heappush(heap,(emp[ID][j+1][0],ID,j+1))
  
 return result_list          

if __name__ == '__main__':
    emp = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
    print(employee_free_time(emp))