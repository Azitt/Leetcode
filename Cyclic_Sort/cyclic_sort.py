class traversal:
    def __init__(self):
        self.array = []
        
    def forward_traversal(self):
        for element in self.array:
            print(element)
        
    def backward_traversal(self):
        for element in reversed(self.array):
            print(element)
## missing number #############################            
def find_missing_number(nums):
    i = 0
    while i < len(nums):
          if nums[i] != i and nums[i]<len(nums):
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
          else:
              i += 1
    for i in range(len(nums)):
        if nums[i] != i:
            return i
                      
    return len(nums)
nums = [0,1,2,4]
print(find_missing_number(nums))

## First Missing Positive#####################
def smallest_missing_positive_integer(nums):   
    i = 0
    while i < len(nums):
        if nums[i] != (i+1) and 0<= (nums[i] -1)< len(nums):
            nums[nums[i]-1],nums[i] = nums[i], nums[nums[i]-1]
        else: 
            i += 1
    for i in range(len(nums)):
        if (i + 1) != nums[i]:
            return i + 1
    return len(nums) + 1  

nums = [7,8,9,10]
print(smallest_missing_positive_integer(nums)) 

## Corrupt pair################################# 
def find_corrupt_pair(nums):
    i = 0
    missing,duplicate = None,None
    while i < len(nums):
        if nums[i] != nums[nums[i]-1]:
            nums[nums[i]-1],nums[i] = nums[i], nums[nums[i]-1]
        else: 
            i += 1
    for i in range(len(nums)):
        if (i + 1) != nums[i]:
            duplicate,missing= nums[i],i+1  
    return missing,duplicate          
nums = [3,1,2,5,2]
print(find_corrupt_pair(nums))  

##  First K Missing Positive Numbers##############
def first_k_missing_numbers(arr, k):  
    
    for i in range(len(arr)):
        if len(arr)>arr[i]>=1 and arr[i] != arr[arr[i]-1] :  
            arr[arr[i]-1] , arr[i] = arr[i], arr[arr[i]-1] 
        else:
            i += 1
    print("arr",arr)        
    no_correct_pos = set()
    miss_arr = []
    for i in range(len(arr)):
        if len(miss_arr) < k:
         if (i+1) != arr[i]:
           no_correct_pos.add(arr[i])
           miss_arr.append(i+1) 
    nextnum = len(arr) + 1  
    print("no_correct_pos,miss_arr",no_correct_pos,miss_arr)     
    while len(miss_arr) < k:
        if nextnum not in no_correct_pos:
           miss_arr.append(nextnum)
        nextnum += 1
    return miss_arr

arr, k = [0,-5,3,1,5,4], 3
print(first_k_missing_numbers(arr, k))        
                                                    