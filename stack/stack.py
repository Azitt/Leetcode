## basic calculator###########################
def calculator(expression):
  stack =[]
  number, sign_value,result = 0,1,0
  for e in expression:
      if e.isdigit():
          number = number*10 + int(e)
      elif e in "+-" : 
          result += number*sign_value
          sign_value = -1 if e== "-"  else 1
          number =0
      elif e == "(":
          stack.append(result)
          stack.append(sign_value)
          result = 0
          sign_value =1
      elif e == ")":
          result += sign_value*number
          pop_sign_value = stack.pop()
          result *= pop_sign_value
          
          second_value = stack.pop()
          result += second_value
          number = 0
  return result + number*sign_value               
          
exp = "(8 + 100) + (13 - 8 - (2 + 1))" 
print(calculator(exp))  

## Remove All Adjacent Duplicates In String#####################
def remove_duplicates(string):
  stack = []
  if len(string) == 1:
        return string
  for s in string:
      if stack and s == stack[-1]:
          stack.pop()
      else:
          stack.append(s) 

  return "".join(stack)
                
string = "ggaabcdeb"
print(remove_duplicates(string))

## Minimum Remove to Make Valid Parentheses ##################
def min_remove_parentheses(s):
    stack = []
    for i in range(len(s)):
        
        if  stack and s[i] ==")" and stack[-1][0] =="(":
            stack.pop()
        elif s[i] in "()":
            stack.append((s[i],i))
    
    new_s = list(s)
    for p in stack:
        new_s[p[1]] = ""
    
    return "".join(new_s)           
                    
s =")((yz)())("
print(min_remove_parentheses(s)) 

## Exclusive Execution Time of Functions################## 
def exclusive_time(n, logs):
    stack = [] 
    result = [0]*n 
    for log in logs:
        log = log.split(":")
        ID = int(log[0])
        s_e = log[1]=="start"
        timestamp = int(log[2])
        if s_e:
            stack.append((ID,timestamp))
        else:
           _, timestamp_pop = stack.pop()
           exec_time = (timestamp - timestamp_pop) + 1
           result[ID] += exec_time 
           
           if stack:
               result[stack[-1][0]] -= exec_time
    return result
                                                  
n = 3
logs = ["0:start:0","0:end:0","1:start:1","1:end:1","2:start:2","2:end:2","2:start:3","2:end:3"]
print(exclusive_time(n, logs))
 