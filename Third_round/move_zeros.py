# we have an array of int move zerros to the end of array
def move_zeros(nums):
   e,c = len(nums)-1,0    
   while c<= e:
        if nums[c] == 0:
            nums[e],nums[c] = nums[c], nums[e]
            e -=1
        elif nums[c] != 0:
            c +=1
   return nums           
nums = [0,1,0,3,0,1] 
print(move_zeros(nums))
nums = [1,0,0,3,9,1] 
print(move_zeros(nums))             