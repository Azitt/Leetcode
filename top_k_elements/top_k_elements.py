from heapq import *

### Kth Largest Element in a Stream ########################
class KthLargest:
    
    def __init__(self,nums,k) -> None:
        self.k = k
        self.min_heap = []
        for num in nums:
            self.add(num)
        
    def add(self,value):
        if len(self.min_heap)< self.k:
            heappush(self.min_heap,value)
        else:
         if value > self.min_heap[0]:
            heappop(self.min_heap) 
            heappush(self.min_heap,value) 
        print(self.min_heap)     
        return self.min_heap[0]        
        
nums = [3,4,5]
nums_coming = [40,50,30,60] 
k = 2
top_k = KthLargest(nums,k) 
for i in range(len(nums_coming)):
       k_largest= top_k.add(nums_coming[i])
       print(k_largest) 

##   Reorganize String


from collections import Counter
def reorganize_string(str):
 s_freq=Counter(str) 
 s_out = ""
 max_heap = []
 prev = None
 for s,freq in s_freq.items():
      heappush(max_heap, (-freq,s))
 while max_heap:
    freq,s = heappop(max_heap) 
    s_out += s
    freq +=1
    if prev:
        heappush(max_heap, prev) 
        prev = None
    if freq != 0:
        prev = (freq,s)
 return s_out        
string = "aaabc"      
print(reorganize_string(string))