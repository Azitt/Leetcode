# more efficient method###########################
def merge_sorted(nums1, m, nums2, n):
  p1 = m -1
  p2 = n -1
  for p in range(m+n -1, -1,-1):
      if p2 < 0:
          break
      if p1 >= 0 and nums1[p1] > nums2[p2]:
          nums1[p] = nums1[p1]
          p1 -=1
      else:
          nums1[p] = nums2[p2]
          p2 -= 1
  return nums1              
## my method##############################
from heapq import *
def merge_sorted(nums1, m, nums2, n):    
 min_heap = []
 i, j = 0,0
 heappush(min_heap,(nums1[0],1,0))
 heappush(min_heap,(nums2[0],2,0))
 sorted_out = []
 while min_heap:
    popped,index_array,index_element = heappop(min_heap)
    sorted_out.append(popped)
    if index_array == 1 and i < m-1:
        i += 1
        heappush(min_heap,(nums1[i],1,i))
    elif index_array == 2 and j < n-1:
        j += 1
        heappush(min_heap,(nums2[j],2,j)) 
 return sorted_out    


m, n = 3,3
nums1 = [3,4,9,0,0,0]
nums2 = [1,2,3]
merge_sorted(nums1, m, nums2, n)

###Kth Smallest Number in M sorted lists########################
from heapq import *
def k_smallest_number(lists,k):    
 min_heap = []
 count = 0
 for list in lists:
     heappush(min_heap,(list[0],count,0))
     count += 1
 sorted_out = []
 while min_heap:
    popped,index_array,index_element = heappop(min_heap)
    sorted_out.append(popped)
    if index_element < len(lists[index_array]) - 1:
        heappush(min_heap,(lists[index_array][index_element+1],index_array,index_element +1))
     
 return sorted_out[k-1] 
### second better solution Kth Smallest Number in M sorted lists########################
from heapq import *
def k_smallest_number(lists,k):    
 min_heap = []
 for index,list in enumerate(lists):
     heappush(min_heap,(list[0],index,0))
 k_smallest, smallest_number = 0,0 
 while min_heap:
    smallest_number,index_array,index_element = heappop(min_heap)
    k_smallest += 1
    
    if k_smallest == k:
        break
    if index_element < len(lists[index_array]) - 1:
        heappush(min_heap,(lists[index_array][index_element+1],index_array,index_element +1))
     
 return smallest_number

lists=[[2,6,8],[3,7,10],[5,8,11]]
k = 5
print(k_smallest_number(lists,k))


##Find K Pairs with Smallest Sums#############################
k = 4
L1 = [3,4,8,9]
L2 = [1,2,5,6]
from heapq import *
max_heap = []
count_k = 0
for i in range(len(L1)):
    for j in range(len(L2)):
        if count_k < k:
            count_k +=1
            sum = L1[i] + L2[j]
            heappush(max_heap,-(sum,[L1[i],L2[j]]))  
        elif count_k >= k and (L1[i] + L2[j]) < -max_heap[0][0]:
            heappop(max_heap) 
            sum = L1[i] + L2[j]
            heappush(max_heap,-(sum,[L1[i],L2[j]]))
print(max_heap)                   