## jump game 1##########################################
def Jump_game_1(nums):
   target = len(nums) -1
   for i in range(len(nums)-2,-1,-1):       
       if target <= i+nums[i]:
           target = i
   if target ==0:
       return True
   return False        
nums = [3,2,1,0,4]    
print(Jump_game_1(nums))

##Boats to save people#####################################

def boat_to_save(people,limit):
 boat_count = 0
 p= sorted(people)
 left,right = 0, len(people) -1
 while left <= right:
  if (p[left] + p[right]) <= limit:
      left += 1
  right -= 1   
  boat_count += 1    

 return boat_count      

people = [3,2,2,1,1]
limit = 3
print(boat_to_save(people,limit)) 

## gas_station####################################
def gas_station(gas,cost):
    if sum(gas)<sum(cost):
        return -1
    start_index = 0
    current_gas = 0
    for i in range(start_index,len(gas)):
        current_gas = current_gas + (gas[i]-cost[i])
        if current_gas< 0:
            current_gas = 0
            start_index = i + 1
    return start_index        
            
gas = [5, 1, 2, 3, 4]
cost = [4, 4, 1, 5, 1]
print(gas_station(gas,cost))

## two city scheduling####################################
def two_city_scheduling(costs):
 sorted_cost = sorted(costs, key=lambda cost:cost[0]-cost[1])
 total_cost = 0
 n = len(sorted_cost)
 for i in range(n//2):
    total_cost += sorted_cost[i][0] + sorted_cost[n - 1 - i][1]    
 return total_cost        

costs = [[20,10],[20,10],[20,10],[20,10]]        
print(two_city_scheduling(costs))  

## Minimum Number of Refueling Stops#######################
      
           
