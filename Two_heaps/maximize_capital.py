
import heapq
def maximum_capital(c,k,capitals,profits):
 cap = []
 for i in range(len(capitals)):
    heapq.heappush(cap,(capitals[i],i))

 profit_max = []
 for _ in range(k):
  while cap and c >= cap[0][0] :
    _, i = heapq.heappop(cap)
    heapq.heappush(profit_max,-profits[i])
  if not profit_max:
     break
  profit = - heapq.heappop(profit_max)  
  c = c + profit 
 return c 


if __name__ == "__main__":  
 capitals = [1,2,2,3]
 profits = [2,4,6,8]
 k = 2
 c = 1
 print(maximum_capital(c,k,capitals,profits))
 

# find Median from Data stream ######################
from heapq import *

class MedianOfStream:
    
    def __init__(self):
        self.max_heap_for_smallnum = []
        self.min_heap_for_largenum = []

    def insert_num(self, num):
        if not self.max_heap_for_smallnum or -self.max_heap_for_smallnum[0] >= num:
            heappush(self.max_heap_for_smallnum, -num)
        else:
            heappush(self.min_heap_for_largenum, num)

        if len(self.max_heap_for_smallnum) > len(self.min_heap_for_largenum) + 1:
            heappush(self.min_heap_for_largenum, -heappop(self.max_heap_for_smallnum))
        elif len(self.max_heap_for_smallnum) < len(self.min_heap_for_largenum):
            heappush(self.max_heap_for_smallnum, -heappop(self.min_heap_for_largenum))

    def find_median(self):
        if len(self.max_heap_for_smallnum) == len(self.min_heap_for_largenum):

            return -self.max_heap_for_smallnum[0] / 2.0 + self.min_heap_for_largenum[0] / 2.0

        return -self.max_heap_for_smallnum[0] / 1.0         

if __name__ == "__main__":
    median_num = MedianOfStream()
    nums = [35, 22, 30, 25, 1]
    numlist = []
    x = 1
    for i in nums:
        numlist.append(i)
        print(x, ".\tData stream: ", numlist, sep="")
        median_num.insert_num(i)
        print("\tThe median for the given numbers is: " +
              str(median_num.find_median()), sep="")
        print(100*"-"+"\n")
        x += 1        
        
## sliding windows median############################

import heapq 
def median_sliding_window(nums, k):

    # Replace this placeholder return statement with your code
    Medium = []
    inp = nums
    for i in range(len(inp)-k + 1) : 
     min_heap = []
     max_heap = []
     for j in range(i, i+k):
        if max_heap and inp[j]> max_heap[0]:
            heapq.heappush(min_heap,inp[j])
        else:
           heapq.heappush(max_heap,-inp[j])  
        if len(max_heap) > len(min_heap) + 1 :
            heapq.heappush(min_heap, - heapq.heappop(max_heap))
        elif len(max_heap) < len(min_heap):                
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
     if len(min_heap)== len(max_heap):
        temp = (-max_heap[0] + min_heap[0])/2
     else:
        temp = -max_heap[0]  
     Medium.append(temp)
    return Medium           
nums = [1,3,-1,2,-2,-3,5,1,5,3] 
k = 4  
median_sliding_window(nums, k)             

### Schedule Tasks on Minimum Machines ###################
machine_count = 0
import heapq
def tasks(tasks_list):

 heapq.heapify(tasks_list)
 machines_available = []
 optimal_machine = 0
 while tasks_list:
    task = heapq.heappop(tasks_list) 
    if machines_available and task[0] >= machines_available[0][0]:
        _,machine_inuse = heapq.heappop(machines_available)  
        heapq.heappush(machines_available,(task[1],machine_inuse))
    else:
     optimal_machine += 1
     heapq.heappush(machines_available,(task[1],optimal_machine)) 
 return  optimal_machine       
