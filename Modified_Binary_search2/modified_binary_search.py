##binary search#################################
nums = [-5,0,2,6,12]
target = 6
start, end = 0, len(nums) -1
index = None
while start <= end:
    mid = start + (end - start)//2
    if target > nums[mid]:
        start = mid + 1
    elif target < nums[mid]:
        end = mid - 1
    else:
        index = mid
        break
print(index)  

## Search in Rotated Sorted Array############################
                    
def binary_search_rotated(nums, target):
 start, end = 0, len(nums) -1
 while start <= end:
    mid = start + (end - start)//2
    
    if target == nums[mid]:
        return mid        
    
    if nums[start]<= nums[end]:
     if target >= nums[start] and target < nums[mid]:
        end = mid - 1
     else:
         start = mid + 1   
    else:     
     if target > nums[mid] and target <= nums[end]:
        start = mid + 1
     else:    
        end = mid - 1          
 return -1

nums = [176,188,199,200,1,2,3]
target = 199
print(binary_search_rotated(nums, target))

##Bad version ############################################
n = 8
array = [1,2,3,4,5,6,7,8]
bad = 6
low,high = 1,n 
API_count = 0
def Calls_API(version,bad):
    if version >= bad:
        return True
    return False
while low <= high:
    mid = low + (high - low)//2
    if not Calls_API(mid,bad):
        low = mid + 1
    else:
        high = mid - 1
    API_count += 1    
  
print([low,API_count])

## randon pick with weight#################################
#the idea here is to show based on this method chance of picking the index with higher value is more than index with lower values
import random
class  RandomPickWithWeight:
    
    def __init__(self,weights):
        self.weight_array = []
        total_weight = 0
        for w in weights:
           total_weight += w
           self.weight_array.append(total_weight)
        self.total_weights = total_weight
    def pick_index(self):
        random_value = random.randint(1,self.total_weights)
        low = 0
        high = len(self.weight_array)- 1
        while low <= high:   
          mid = low + (high - low)//2
          if random_value > self.total_weights[mid]:
              low = mid + 1
          else:
              high = mid - 1
        return low          
          
#### find k closet elements####################
nums = [1,2,3,4,5] 
k = 4
target = 3
low,high = 0, len(nums) - 1 
out = []
while low <= high:
    mid = low + (high - low)//2
    if abs(nums[mid+1] - target) < abs(nums[mid-1] - target):        
        low = mid + 1
    else:
        high = mid - 1  
    out.append(nums[mid])        
print(out)
def findClosestElements(arr,k,x):
		# initially, consider if the starting point can exist in any of the first (length of array - k) elements
		l = 0
		r = len(arr) - k

		# we use binary search to find the start point in the array
		# we check if the mid point difference at any mid is greater than mid + k, if it is then we dont have to consider elements before mid as the starting point and move our l closer to r
		# else if it is less than the mid + k elements than we bring our r closer to l

		while l < r:
			mid = l + (r - l) // 2

			if x - arr[mid] > arr[mid + k] - x:
				l = mid + 1
			else:
				r = mid

		# finally we have our starting point, then just iterate k times from l and add the answer

		ans = []
		for i in range(k):
			ans.append(arr[l + i])

		return ans
nums = [1,2,3,4,5] 
k = 4
target = 3
print(findClosestElements(nums,k,target))          