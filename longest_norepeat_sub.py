
def find_longest_substring(input_str):
 s = input_str
 start = 0
 hash_map = {}
 len_max = 0
 for end in range(len(s)):
    c = s[end]
    if c not in hash_map:
        hash_map[c] = end
    else:
        print(hash_map)
        if hash_map[c] >= start:
         if end - start  > len_max:
            len_max = end - start 
            print(len_max)
         start =hash_map[c] +1   
        hash_map[c] = end 
 end += 1        
 if end - start  > len_max:
  len_max = end - start         
 return len_max 

print(find_longest_substring("pwwkew"))            