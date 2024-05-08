##naive approach############################### 
def word_break2(s,word_dict):
    def backtrack(prefix,suffix):
     if not suffix:
        return [prefix]
     result = []
     for word in word_dict:
        if suffix.startswith(word):
            result.extend(backtrack(prefix+[word],suffix[len(word):]))
     return result       
            
    return backtrack([],s) 

s = "catsanddog"
word_dict = ["cat", "cats", "and", "sand", "dog"]
print(word_break2(s, word_dict))
###dynamic programming approach#########################
def word_break2(s, word_dict):
    dp = [[]] * (len(s) + 1)
    dp[0] = [""]

    for i in range(1, len(s) + 1):

        prefix = s[:i]

        temp = []

        for j in range(0, i):
            suffix = prefix[j:]
            
            if suffix in word_dict:
                
                for substring in dp[j]:
                    temp.append((substring + " " + suffix).strip())

        dp[i] = temp

    return dp[len(s)]
s = "catsanddog"
word_dict = ["cat", "cats", "and", "sand", "dog"]
print(word_break2(s, word_dict))

###Decode Ways ########################################### 
def num_of_decodings(decode_str):
  n = len(decode_str)
  dp = [0]*(n+1)
  dp[0]= 1
  if decode_str[0] != 0:
      dp[1] = 1
  else:    
      return 0
  
  for i in range(2,n+1):
      if decode_str[i-1] != '0':
          dp[i] += dp[i-1] 
      if decode_str[i-2] =='1' or (decode_str[i-2] == '2' and decode_str[i-1]<='6'):
          dp[i] += dp[i-2]    
  return dp[n]                


decode_str = "124"
print(num_of_decodings(decode_str))

### Climbing Stairs##########################################
def climb_stairs(n):   
    dp = [0]*(n+1)
    dp[0],dp[1] = 1,1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]    
print(climb_stairs(4))











                 