## Design HashMap ########################################
class DesignHashMap():
    def __init__(self):        
        self.key_size = 2069
        self.hash_map = [[] for _ in range(self.key_size)]
    
    def put(self,key,value):
        hash_key = key%self.key_size
        found = False
        if self.hash_map:
         for i, kv in enumerate(self.hash_map[hash_key]):
            if hash_key ==kv[0]:
             self.hash_map[hash_key][i] = (hash_key,value)
             found =True
             break
        if not found:     
         self.hash_map[hash_key].append((hash_key,value)) 
    def get(self,key):
        hash_key = key%self.key_size
        for k , v in self.hash_map[hash_key]:
            if hash_key == k:
              return v
        return -1
    def remove(self,key):
        hash_key = key%self.key_size
        for i,kv in enumerate(self.hash_map[hash_key]):
            if hash_key == kv[0]:
              del self.hash_map[i]  
              break        

input_hash_map = DesignHashMap()
keys = [5, 2069, 2070, 2073, 4138, 2068] 
values = [100, 200, 400, 500, 1000, 5000]
funcs = ["Get", "Get", "Put", "Remove"]
func_keys = [[5], [2073], [2073, 250], [2073]]


for i in range(len(keys)):
    # print(keys[i]%2069)
    input_hash_map.put(keys[i], values[i])
 
   
for i in range(len(funcs)):  
    if funcs[i] == "Put":
        input_hash_map.put(func_keys[i][0], func_keys[i][1])
    elif funcs[i] == "Get":
        input_hash_map.get(func_keys[i][0]) 
    elif funcs[i] == "Remove":
        input_hash_map.remove(func_keys[i][0]) 
 
## Fraction to Recurring Decimal ###############################
def fraction_to_decimal(numerator, denominator):
    result = ""
    hash_map = {} 
    if (numerator < 0) ^ (denominator < 0):
        result += "-"
        numerator, denominator = abs(numerator), abs(denominator)
    if numerator == 0:
        return 0
    qu = numerator//denominator
    rem = (numerator%denominator)*10
    result += str(qu)
    if rem == 0:
        return result
    else:
        result += "." 
        while rem != 0:
         if rem in hash_map:
             begin = hash_map[rem]
             left = result[0:begin]
             right = result[begin+1:len(result)]
             result = left + "(" + right + ")"
             return result   
         hash_map[rem] = len(result)
         qu = rem//denominator
         result += str(qu)
         rem = (rem%denominator)*10
        return result

print(fraction_to_decimal(2, 4))     

### Logger Rate Limiter ###########################
class RequestLogger:
    def __init__(self, time_limit):
        self.hash_map = {}
        self.time_limit = time_limit
    def request(self,timestamp, request):
        if request in self.hash_map:
            if abs(timestamp - self.hash_map[request]) < self.time_limit:
                return False
    
        self.hash_map[request] = timestamp
        return True
req_class = RequestLogger(7)            
req=[[1,"good morning"],[5,"good morning"],[9,"i need coffee"],[10,"hello world"],[11,"good morning"],[15,"i need coffee"],[17,"hello world"],[25,"i need coffee"]]                
for r in req:
    print(req_class.request(r[0],r[1])) 

## Next Greater Element #######################             
def next_greater_element(nums1,nums2):
    stack = []
    hash_map = {}
    result = []*len(nums1)
    for num in nums2:            
       if stack and num > stack[-1]:
           popped = stack.pop()
           hash_map[popped] = num 
       stack.append(num)
                     
    for num in nums1:       
      result.append(hash_map.get(num,-1))      
    return result

nums1,nums2 = [1,2,3], [1,2,3,4,5]
print(next_greater_element(nums1,nums2)) 

nums1,nums2 = [5,3,4], [2,4,5,3]
print(next_greater_element(nums1,nums2))

## Isomorphic Strings #################################
def  Isomorphic_Strings(string1,string2):
    hash_map1,hash_map2 = {}, {}
    for s1,s2 in zip(string1,string2):
        if (s1 in hash_map1 and s2 != hash_map1[s1]) or (s2 in hash_map2 and s1 != hash_map2[s2]):
            return False
        hash_map1[s1] = s2
        hash_map2[s2] = s1
    return True            
string1,string2 = "egg", "all"
print(Isomorphic_Strings(string1,string2))
string1,string2 = "foo","bar"
print(Isomorphic_Strings(string1,string2))

## Longest Palindrome ############################
from collections import Counter
def longest_palindrome(string):
    string_hash = Counter(string)
    length = 0
    for s,f in string_hash.items():
        pair = f//2
        length += pair
    length *= 2
    
    if length < len(string):
        length += 1
    return length

string = "opinion"
print(longest_palindrome(string))        