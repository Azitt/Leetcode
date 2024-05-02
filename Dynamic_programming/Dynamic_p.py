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