## Fibonacci series##################
# naive approach which can have high time complexity
def fib(n):
 if n <= 2:
    return n
 return fib(n-1) + fib(n-2)

print(fib(4))

# better approach is dynamic programming####################
## top-dowm approach        
def fib_memo(n,memo ={}):
    if n in memo:
        return memo[n]
    if n <=1:
        return n
    memo[n] = fib_memo(n-1,memo) + fib_memo(n-2,memo)
    print("memo,n",memo,n)
    return memo[n]
print(fib_memo(4))
## bottom-up approach##################################        
def fib_tabulation(n):
    lookup = [0]*(n+1)
    lookup[1] = 1
    for i in range(2,len(lookup)):
        lookup[i] = lookup[i-1] + lookup[i-2]
    return lookup[n]    
print(fib_tabulation(4)) 

## Knapsack#################################################
# we make a table which rows=items+1,cols=capacity+1, and with every new item we check 
# if we can include new item or not based on the max value we got sofar and the value of current item

def find_max_knapsack_profit(capacity, weights, values):
    # Create a table to hold intermediate values
    n = len(weights)
    dp = [[0 for i in range(capacity + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):

            # Check if the weight of the current item is less than the current capacity
            if weights[i-1] <= j:
                dp[i][j] = max(values[i-1] + dp[i-1][j-weights[i-1]], 
                              dp[i-1][j])
                            
            # We don't include the item if its weight is greater than the current capacity
            else:
                dp[i][j] = dp[i-1][j]

    return dp[-1][-1] #[n][capacity]     

weights = [1, 2, 3, 5] 
values = [1, 5, 4, 8]
capacity = 6
print(find_max_knapsack_profit(capacity, weights, values))  

###Coin Change##################################################### 
def calculate_minimum_coins(coins, rem, counter):  #Helper function that calculates amount left to be calculated and tells what it's value can be.
    if rem < 0: 
        return -1
    if rem == 0:
        return 0
    if counter[rem - 1] != float('inf'):
        return counter[rem - 1]
    minimum = float('inf')

    for s in coins: #Recursive approach to keep in account every number's result 
        result = calculate_minimum_coins(coins, rem - s, counter)
        # print("result,rem,minimum",result,rem,minimum)
        if result >= 0 and result < minimum:
            minimum = 1 + result
        # print("minimum",minimum)
    counter[rem - 1] =  minimum if minimum !=  float('inf') else  -1 
    return counter[rem - 1]

def coin_change(coins, total): #Main function
    if total < 1:
        return 0
    return calculate_minimum_coins(coins, total, [float('inf')] * total)

coins =[1,2,3]
total = 5
coin_change(coins, total)  

### Tribonachi number##########################
# my solution###########################
def Tribonachi (n) :
    lookup = [-1]*(n+1) 
    lookup[0] = 0
    lookup[1] = 1
    lookup[2] = 1
    for i in range(3,len(lookup)):
        lookup[i] = lookup[i-1] + lookup[i-2] + lookup[i-3]
    return lookup[n]  
print(Tribonachi (7)) 

### better solution##################### 
def find_tribonacci(n):
    if n < 3:
        return 1 if n else 0

    first_num, second_num, third_num = 0, 1, 1
    for _ in range(n - 2):
        first_num, second_num, third_num = second_num, third_num, \
          first_num + second_num + third_num
    return third_num

## Partition Equal Subset Sum##############################
#naive approach########################
def canPartition(nums):
    total_sum = sum(nums)
    # If the total sum is odd, it cannot be partitioned into two equal subsets
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2

    def dfs(current_index, current_sum):
        # Base cases
        if current_sum == target:
            return True
        if current_sum > target or current_index >= len(nums):
            return False
        
        # Recurse by including the current number
        include = dfs(current_index + 1, current_sum + nums[current_index])
        # Recurse by not including the current number
        exclude = dfs(current_index + 1, current_sum)

        return include or exclude
    
    return dfs(0, 0)

print(canPartition([1, 5, 11, 5]))

## dynamic programming approach############################
def can_partition_array(nums):

    array_sum = sum(nums)
    
    if array_sum % 2 != 0:
        return False
    
    subset_sum = array_sum//2

    dp = [[False for i in range(len(nums)+1)] for j in range(subset_sum + 1)]
    
    for i in range(0, len(nums) + 1):
        dp[0][i] = True
    
    for i in range(1, subset_sum + 1):
        for j in range(1, len(nums)+1):
            if nums[j - 1] > i:
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = dp[i - nums[j - 1]
                                      ][j - 1] or dp[i][j - 1]
              
    return dp[subset_sum][len(nums)]

###Counting Bits###########################################################
def bits_count(n):
    array = [0]*(n+1)
    if n ==0:
        return array
    array[0] = 0
    array[1] = 1
    for i in range(n+1):
        if i%2==0:
            array[i] = array[i//2]
        else:
            array[i] = array[i//2] + 1    
    return array
## 01 MAtrix########################################
import math
def update_math(mat):
    m,n = len(mat), len(mat[0])
    
    for r in range(m):
        for c in range(n):
            if mat[r][c] > 0:
                above = mat[r-1][c] if r> 0 else math.inf
                left = mat[r][c-1]  if c > 0 else math.inf
                mat[r][c] = min(above,left) + 1
    for r in range(m-1,-1,-1):
        for c in range(n-1,-1,-1):
            if mat[r][c] >0:
             bottom = mat[r+1][c] if r > m-1 else math.inf
             right = mat[r][c+1]  if c > n-1 else math.inf
             mat[r][c] = min(mat[r][c],bottom+1,right+1) 
    return mat

mat = [[0, 0, 1], [0, 1, 1], [1, 0, 1]]
print(update_math(mat))  

## House Robber II ####################################

def house_robbery_helper(money):
    lookup = [0]*(len(money)+1)
    lookup[1] = money[0]
    for i in range(2,len(money)+1):   
        lookup[i] = max(lookup[i-2]+money[i-1],lookup[i-1])
    return lookup[-1]    

def house_robbery(money): 
    set1 =money[:-1]
    set2 = money[1:]
    print(set1,set2)
    return max(house_robbery_helper(money[:-1]),house_robbery_helper(money[1:]))
                         

money = [7,4,1,9,3]
print(house_robbery(money))

## Maximum Product Subarray################################
def max_product(nums):
    if len(nums) == 0:
        return 0
    min_product, max_product = nums[0], nums[0]
    product = max_product
    for i in range(1,len(nums)):
        
        prev_max_product = max_product
        max_product = max(min_product*nums[i],max_product*nums[i],nums[i])
        min_product = min(min_product*nums[i],prev_max_product*nums[i],nums[i])
        
        
        product = max(product,max_product)
    return product 

print(max_product([2,3,-2,4]))   
             
## Combination Sum####################################
             
                      