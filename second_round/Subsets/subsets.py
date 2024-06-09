###subset##############################################
def get_bit(num,bit):
    temp = 1<< bit
    temp = temp&num
    if temp == 0:
        return 0
    return 1
def find_all_subsets(nums):
 subsets_count = 2**len(nums)
 subsets = []
 for i in range(subsets_count):
    subset = set()
    for j in range(len(nums)):
     # if returns 1 it indicats that the jth bit is set to 1
     if get_bit(i,j)==1 and nums[j] not in subset:
            subset.add(nums[j])
    if i==0:
        subsets.append([])
    else:
        subsets.append(subset)
 return subsets 

nums = [3,6,9]
print(find_all_subsets(nums)) 

##Permutations##################################################

def swap_char(curr_index,i,word):
    word = list(word)
    word[curr_index], word[i] = word[i], word[curr_index]
    return ''.join(word)

def permute_rec(current_index,word,result): 
    if current_index == len(word) - 1:
        result.append(word) 
        return  
    for i in range(current_index,len(word)):
      swap_string = swap_char(current_index,i,word)
      permute_rec(current_index+1,swap_string,result)
      
def permute_word(word):
    result = []
    permute_rec(0,word,result)  
    return result  
word = "kop"
print(permute_word(word))   

##Letter combination of phone number############################

def letter_combination_rec(index,path,digits,letters,combinations):
    if len(path) == len(digits):
        combinations.append(''.join(path))
        return
    digit_letters = letters[digits[index]]
    if digit_letters:
        for letter in digit_letters:
          path.append(letter)
          letter_combination_rec(index+1,path,digits,letters,combinations) 
          path.pop() 
        
     
def letter_combinations(digits):
 if len(digits) == 0:
    return []
 else:
      digits_mapping = {
        "1": [""],
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]}
 list_result = []
 letter_combination_rec(0,[],digits,digits_mapping,list_result)    
 return list_result            

digits = "23"
print(letter_combinations(digits)) 

##Generate Parentheses######################
def Generate_Parentheses_rec(n,open_count,close_count,path,out_list):
    if open_count == n and close_count==n:
        out_list.append(''.join(path))
    else:
     if open_count < n:
        path.append('(')
        Generate_Parentheses_rec(n,open_count+1,close_count,path,out_list)
        path.pop()
     if close_count < n:
        path.append(')')
        Generate_Parentheses_rec(n,open_count,close_count+1,path,out_list) 
        path.pop()   
        
def Generate_Parentheses(n):
    out_list = []
    Generate_Parentheses_rec(n,0,0,[],out_list) 
    return out_list   

print(Generate_Parentheses(3))

## Find K-Sum Subsets########################################
def get_bit(num,bit):
    temp = 1<<bit
    temp = temp&num
    if temp == 0:
        return 0
    return 1
def get_k_sum_subsets(nums,k):
    subset_count = 2**len(nums)
    subsets = []
    for i in range(subset_count):
        subset = []
        for j in range(len(nums)):
            if get_bit(i,j) == 1 and nums[j] not in subset:
                subset.append(nums[j])
        if sum(subset) == k:
            subsets.append(subset)        
    return subsets
# nums=[1,3,5,21,19,7,2]
# k = 10

nums, k= [8,13,3,22,17,39,87,45,36] , 3
print(get_k_sum_subsets(nums,k))
