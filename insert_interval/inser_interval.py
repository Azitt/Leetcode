# def insert_interval(existing_intervals, new_interval):

#   # Replace this placeholder return statement with your code
#   output_list = []
#   i = 0
#   for i in range(len(existing_intervals)):
#     if new_interval[0] >= existing_intervals[i][1]:
#        print(output_list)
#        if new_interval[0] == existing_intervals[i][1]:
#          output_list.append([existing_intervals[i][0],max(existing_intervals[i][1],new_interval[1])])
#        else:  
#         output_list.append(existing_intervals[i])
  
#   print("here",output_list)      
#   for j in range(len(existing_intervals)): 
#       if output_list[-1][1] >= existing_intervals[j][0]: 
#          output_list[-1][1] = max(output_list[-1][1],existing_intervals[j][1])
#       else:
#          output_list.append(existing_intervals[j])   
#   print(output_list)
#   return output_list

# existing_intervals = [[1,2],[3,4],[5,8],[9,15]]
# new_interval = [2,5]

# insert_interval(existing_intervals, new_interval)


def insert_interval(existing_intervals, new_interval):

  # Replace this placeholder return statement with your code
  output_list = []
  i = 0
  while i < len(existing_intervals) and new_interval[0] > existing_intervals[i][1]:
    #    print(output_list)
    #    if new_interval[0] == existing_intervals[i][1]:
    #      output_list.append([existing_intervals[i][0],max(existing_intervals[i][1],new_interval[1])])
    #    else:  
        output_list.append(existing_intervals[i])
        i += 1 
  if output_list is not None:
    if output_list[-1][1] >= new_interval[0]: 
         output_list[-1][1] = max(output_list[-1][1],new_interval[1])
    else:
         output_list.append(new_interval)
  else:
      output_list.append([min(existing_intervals[0][0],new_interval[0]),max(existing_intervals[i][1],new_interval[1])])      
  print("here",output_list)      
  while i < range(len(existing_intervals)): 
      if output_list[-1][1] >= existing_intervals[i][0]: 
         output_list[-1][1] = max(output_list[-1][1],existing_intervals[i][1])
      else:
         output_list.append(existing_intervals[i])  
      i += 1    
  print(output_list)
  return output_list