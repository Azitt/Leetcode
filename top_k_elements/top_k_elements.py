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

### K Closest Points to Origin##########################
# list = [[-1,-3],[-4,-5],[-2,-2],[-2,-3]]
from heapq import *
import math
list = [[1,3],[3,4],[2,-1]]
k= 2
max_heap = []

for l in list:
    distance = math.sqrt(l[0]**2 +l[1]**2)
    if len(max_heap) < k:    
        heappush(max_heap,(-distance,l))
    else:
        if distance < -max_heap[0][0]:
            heappop(max_heap)
            heappush(max_heap,(-distance,l))  
print([h[1] for h in max_heap])  

### Top K Frequent Elements##################
arr = [1,3,5,14,18,14,5]
k = 2
hash_map = {}
min_heap = []
for a in arr: 
    hash_map[a] = hash_map.get(a,0) + 1
for key,value in hash_map.items():
    
    if len(min_heap) < k:
        heappush(min_heap,(value,key))
    else:
        if value > min_heap[0][0]:
            heappop(min_heap)
            heappush(min_heap,(value,key))
print([h[1] for h in min_heap])            
                               
### Kth Largest Element in an Array#############
arr = [6,8,7,5,9,4,2,3]
k = 6
min_heap = []
for a in arr:
    if len(min_heap) < k:
        heappush(min_heap,a)
    else:
        if a > min_heap[0]:
            heappop(min_heap)
            heappush(min_heap,a) 
print(min_heap[0])               

### K frequent words##############################
#this method is not acceptable because it says in statement Sort the frequencies from highest to lowest and then return the top 
#𝑘 frequent words. Words with the same frequency should be sorted by their lexicographical order.

string = ["lets","play","cricket","and","then","lets","play","badminton"]
k = 3  
from collections import Counter
string_dict = Counter(string)
min_heap = []
for key,value in string_dict.items():
        heappush(min_heap,(value,key))
        if len(min_heap)> k:
            heappop(min_heap) 
print(sorted([h[1] for h in min_heap]))  

### correct way############################
string = ["lets","play","cricket","and","then","lets","play","badminton"]
k = 3  
from collections import Counter
string_dict = Counter(string)
max_heap = []
out_array = []
for key,value in string_dict.items():
        heappush(max_heap,(-value,key)) 
        
for _ in range(k):
    _,key = heappop(max_heap)
    out_array.append(key)   
print(out_array)                                              