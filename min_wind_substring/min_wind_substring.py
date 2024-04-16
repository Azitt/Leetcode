def min_window(s, t):
 hash_map1, hash_map2= {}, {}
 
 for t1 in t:
    hash_map2[t1] =  hash_map2.get(t1,0) + 1
    
 len_min = float("inf")
 start = 0
 out = [-1,-1]
 current, required = 0, len(hash_map2)
 
 for end in range(len(s)): 
        
    if s[end] in t:
        hash_map1[s[end]] =  hash_map1.get(s[end],0) + 1
    if s[end] in hash_map2 and hash_map1[s[end]]== hash_map2[s[end]]:
           current +=1
    while current== required:       
        if end - start +1 < len_min:
         len_min = (end-start+1)
         out = [start,end]
        if s[start] in t: 
         hash_map1[s[start]] -= 1
        if s[start] in hash_map2 and hash_map1[s[start]] < hash_map2[s[start]]: 
            current -=1
        start +=1
 start , end = out    
 return s[start:end+1]  if  len_min != float("inf") else ""        