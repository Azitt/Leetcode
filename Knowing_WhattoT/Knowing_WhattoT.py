## contains duplicate###############
def contains_duplicate(nums,k):
    hash_map = {}
    for i , n in enumerate(nums):
        if n in hash_map and abs(i - hash_map[n]) <= k:
            return True
        hash_map[n] = i
    return False    
nums = [1,2,3,1,5,4]
k = 4
print(contains_duplicate(nums,k))            
## count prefix#######################
def count_prefixes_of_string(s, words):
    # Generate all possible prefixes of the given string
    prefixes = {s[:i] for i in range(1, len(s) + 1)}
    print(prefixes)
    # Count the words that are in the set of prefixes
    count = 0
    for word in words:
        if word in prefixes:
            count += 1
            
    return count

# Example usage
s = "bba"
words = ["b", "c", "bb", "bc", "bba", "abc"]
print(count_prefixes_of_string(s, words))  # Output: 3

## Palindrome Permutation #######################
from collections import Counter
def palindrome_permut(string):
    string_map = Counter(string)
    print(string_map)
    count_odd = 0
    for _,f in string_map.items():
        count_odd += f%2
    if count_odd <= 1:
        return True
    return False    

string = "baefeab"
print(palindrome_permut(string))

## Valid Anagram #################################
def validate_anagram(str1,str2):
    if len(str1) != len(str2):
        return False
    hash_map ={}
    for s in str1:
        hash_map[s] = hash_map.get(s,0) + 1
    for s in str2:
        hash_map[s] = hash_map.get(s,0) - 1
    return all(f == 0 for f in hash_map.values())        

str1, str2 = "anagram", "nagaram"
print(validate_anagram(str1,str2))

## Design Tic-Tac-Toe ############################
from print_tictactoe import print_tic_tac_toe
from print_tictactoe import print_board_states
class TicTacToe():
    # we creat the board here which is an n*n board(row*col)
    def __init__(self,n):
        self.rows = [0]*n
        self.cols = [0]*n
        self.n = n
        self.diagonal = 0
        self.antidiagonal = 0
        # to print the board to visually see what is going on############
        self.board =[["-" for _ in range(n)] for _ in range(n)]
        print_tic_tac_toe(self.board,n)
    # row,col identify cell to mark and player identify who marked the cell     
    def move(self,row,col,player):
        current_player = -1
        if player == 1:
            current_player = 1
        ## check diagonal and antidiagonal#############
        if row==col:
            self.diagonal += current_player
        if col == (self.n - row - 1):
            self.antidiagonal += current_player        
        ## check the ros and cols######################
        self.rows[row] += current_player
        self.cols[col] += current_player
        ## determine the winner########################
        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.antidiagonal) == self.n or abs(self.diagonal) == self.n:
            return player
        return 0                
n = 3
inputs = [[0, 1, 1], [1, 0, 2], [2, 1, 1], [1, 2, 2], [0, 2, 1], [2, 2, 2], [1, 1, 1]]
tic_tac_toe_obj = TicTacToe(n)
for i in range(0, len(inputs)):
     win = tic_tac_toe_obj.move(inputs[i][0], inputs[i][1], inputs[i][2])
     if (win == 0):
        print("\tNo one wins the game")
        print("-" * 100)
     else:
        print("\tPlayer", win, "wins the game")
        print("-" * 100)
        break

## Group Anagrams ##############################
from collections import defaultdict 
def group_anagram(strings):
    hash_map = defaultdict(list)
    for string in strings:   
        key_alpha = [0]*26
        for c in string:
            index = ord(c) - ord('a')
            key_alpha[index] +=1
        hash_map[tuple(key_alpha)].append(string) 
    return hash_map.values() 

strs = ["eat","beat","neat","tea"]
print(group_anagram(strs)) 

## Maximum Frequency Stack #####################
class FreqStack():
    def __init__(self):
        self.frequency ={} 
        self.group = {}
        self.max_freq = 0
    def push(self,value):
  
        self.group[value] = self.group.get(value,0) + 1

        if self.group[value] in self.frequency and value not in self.frequency[self.group[value]]:
            self.frequency[self.group[value]].append(value) 
        else:
            self.frequency[self.group[value]] = [value]    
            
        if self.group[value]> self.max_freq:
                self.max_freq = self.group[value]  
                                     
    def pop(self):
        value_popped = ""
        if self.max_freq > 0:
            value_popped = self.frequency[self.max_freq].pop()
            self.group[value_popped] -= 1
            if not self.frequency[self.max_freq]:
                self.max_freq -= 1
        else:
            return -1
        return value_popped         
                    

inputs = [5, 7, 7, 7, 4, 5, 3]
obj = FreqStack() 
for i in inputs:
    obj.push(i) 
for i in range(len(inputs)):
        print("\t Value removed from stack is: ", obj.pop(), sep="")  

## First Unique Character in a String ###########################
def first_unique_char(s):
    hash_map = {}
    for c in s:
        hash_map[c] = hash_map.get(c,0) + 1
    for i,c in enumerate(s):    
        if hash_map[c] == 1:
            return i    
    return -1    
s = "goodmorning" 
print(first_unique_char(s)) 

## Find All Anagrams in a String ################################
def find_anagrams(a, b): 
    if len(b) > len(a): 
     return []
    hash_b = {}
    output = []
    for c in b:
        hash_b[c] = hash_b.get(c,0) + 1
    w = len(b)    
    for i in range(len(a) -w +1):
        hash_a = {}
        for j in range(i,i+w):
         hash_a[a[j]] = hash_a.get(a[j],0) + 1
         if hash_a == hash_b:
            output.append(i)
    return output                       

a,b = "abab" , "ab"        
print(find_anagrams(a, b))  

## Longest Palindrome by Concatenating Two-Letter Words ################
def longest_palindrome(words): 
    count = 0
    central = False
    frequencies = {} 
    for c in words:
        frequencies[c] = frequencies.get(c,0) + 1
    for word,f in frequencies.items():
        ## palindrome word
        if word[0]==word[1]:
            if f%2 == 0:
              count += f
            else:
              count += f -1
              central = True
        ## none palindrome word      
        elif word[1]>word[0]:
           if (word[1]+word[0]) in  frequencies:
            count += 2*min(f,frequencies[word[1]+word[0]]) 
    if central:
        count += 1
    return count*2                        
                    

words = ["aa","xx","cd","xx","cc","xx","cc","aa"]
print(longest_palindrome(words))

## Ransom Note ###################
def can_construct(ransom_note, magazine):
   magazine_map = {}
   for c in magazine:
       magazine_map[c] = magazine_map.get(c,0) + 1
   for c in ransom_note:
       if (c in magazine_map and magazine_map[c] ==0) or (c not in magazine_map):
           return False
       magazine_map[c] -=1
   return True         
ransom_note = "code"
magazine = "abcodf" 
print(can_construct(ransom_note, magazine))   