nums = [2,3,1,2,4,3]
target = 7
start = 0
s = 0
min_len = float("inf")
for end in range(len(nums)):
    s += nums[end]
    
    while s >= target:
       if  end - start +1 < min_len:
           min_len = end - start + 1
       s -= nums[start]
       start += 1
    
print(min_len)              