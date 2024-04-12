
from collections import deque

# function to clean up the deque
def clean_up(i, current_window, nums):
    while current_window and nums[i] >= nums[current_window[-1]]:
        current_window.pop()

# function to find the maximum in all possible windows
def find_max_sliding_window(nums, w):
    if len(nums) == 1:
        return nums
    output = []
    current_window = deque()
    for i in range(w):
        clean_up(i, current_window, nums)
        current_window.append(i)
    output.append(nums[current_window[0]])
    for i in range(w, len(nums)):
        print(current_window)
        clean_up(i, current_window, nums)
        print(current_window)
        if current_window and current_window[0] <= (i - w):
            current_window.popleft()
        current_window.append(i)
        output.append(nums[current_window[0]])
    return output


def find_max_sliding_window(nums, w):
    heap =[]
    for i in range(len(nums) -w+1):
      maxs = max(nums[i:i+w])
      heap.append(maxs)
    return heap 

print(find_max_sliding_window([3,1,-4,5,3,7,8], 3))