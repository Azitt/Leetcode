### Compilation Order###########################
from collections import deque
def find_compilation_order(dependencies):
  sorted_order = []
  graph = {}
  indegree = {}
  for x in dependencies:
      parent,child = x[1], x[0]
      graph[parent],graph[child] = [], []
      indegree[parent], indegree[child] = 0,0
  if len(graph)<0:
      return sorted_order

  for d in dependencies:
      parent, child = d[1],d[0]
      graph[parent].append(child)
      indegree[child] += 1
    
  sources = deque()
  for key in indegree:
      if indegree[key] == 0:
          sources.append(key)  
  while sources:
      vertex = sources.popleft()
      sorted_order.append(vertex)
      for child in graph[vertex]:
          indegree[child] -=1
          if indegree[child] == 0:
              sources.append(child)
  if len(sorted_order) != len(graph):
      return []
  return sorted_order                            

dependencies = [["B","A"],["C","A"],["D","C"],["E","D"],["E","B"]]
find_compilation_order(dependencies)

### Alien Dictionary################################
from collections import defaultdict, Counter, deque

def alien_order(words):
  adj_list = defaultdict(set)
  counts = Counter({c:0 for word in words for c in word})
  print(counts)
  
  for word1, word2 in zip(words, words[1:]):
        for c, d in zip(word1, word2):
            if c != d:
                if d not in adj_list[c]:
                    adj_list[c].add(d)
                    counts[d] += 1
                break

        else:  
            if len(word2) < len(word1):
                return ""
  result = []
  sources_queue = deque([c for c in counts if counts[c] == 0])
  while sources_queue:
        c = sources_queue.popleft()
        result.append(c)

        for d in adj_list[c]:
            counts[d] -= 1
            if counts[d] == 0:
                sources_queue.append(d)

  if len(result) < len(counts):
        return ""
  return "".join(result)
    
words = ["xro","xma","per","prt","oxh","olv"]
print(alien_order(words)) 

## Verifying an Alien Dictionary ########################################
from collections import defaultdict, Counter, deque

def verify_alien_dictionary(words, order):
  if len(words) == 1:
        return True
  counts = {c:i  for i,c in enumerate(list(order))}
  for w1 ,w2 in zip(words,words[1:]):
      if len(w2) < len(w1):
                return False
      for c1 , c2 in zip(w1,w2):
          if c1 != c2 and counts[c1] > counts[c2]:
              return False
          else:    
              break
      
  return True            

words = ["passengers","to","the","unknown"]
order =  "ptuabcdefghijklmnoqrsvwxyz" 
print(verify_alien_dictionary(words, order))  

## Course Schedule II##################################################
def course_schedule2(n,prerequisites):
    graph = {}
    indegree = {}
    result = []
    if n <= 0:
        return []
    
    for p in prerequisites:
        parent,child = p[1],p[0]
        graph[parent],graph[child] = [], []
        indegree[parent],indegree[child] = 0,0

    for p in prerequisites:
        parent, child = p[1], p[0]
        graph[parent].append(child)
        indegree[child] += 1
    source = deque()
    for child in indegree:
        if indegree[child] == 0:
            source.append(child) 
    while source:
        vertex =source.popleft()
        result.append(vertex)
        for child in graph[vertex]:
            indegree[child] -= 1
            if indegree[child] ==0:
                source.append(child)
    if len(result) != n:
        return []             
    return result                          

n = 5
prerequisites =[[1,0],[2,0],[3,1],[4,3]] 
print(course_schedule2(n,prerequisites)) 

## Course Schedule ################################################  
def course_schedule(n,prerequisites):
    graph = {}
    indegree = {}
    counter = 0
    if n <= 0:
        return []
    
    for p in prerequisites:
        parent,child = p[1],p[0]
        graph[parent],graph[child] = [], []
        indegree[parent],indegree[child] = 0,0

    for p in prerequisites:
        parent, child = p[1], p[0]
        graph[parent].append(child)
        indegree[child] += 1
    source = deque()
    for child in indegree:
        if indegree[child] == 0:
            source.append(child) 
    while source:
        vertex =source.popleft()
        counter +=1
        for child in graph[vertex]:
            indegree[child] -= 1
            if indegree[child] ==0:
                source.append(child)
                 
    return counter == n                          
 
n = 3
prerequisites =[[1,0],[2,1],[1,2]] 
print(course_schedule(n,prerequisites)) 

## Find All Possible Recipes #############################
# def recipes2(recipes,ingredients,supplies):
#     result =[]
#     for i,ing in enumerate(ingredients):
#         valid = True
#         for g in ing:
#             if g not in supplies:
#                 valid = False
#                 break 
#         if valid:
#             result.append(recipes[i]) 
#     return result
# recipes = ["tea", "omelette"]
# ingredients =  [["milk", "caffeine", "sugar"], ["salt", "egg", "pepper"]] 
# supplies = ["salt", "milk", "egg", "caffeine", "sugar"]
# print(recipes2(recipes,ingredients,supplies))
################
def recipes2(recipes,ingredients,supplies):
    result =[]
    valid = True
    available_supply = set (supplies)
    while valid:
     valid = False
     for i,recipe in enumerate(recipes):
        if recipe in available_supply:
             continue
        if all(ing in supplies for ing in ingredients[i]):
            available_supply.add(recipe)
            result.append(recipe)
            valid = True 
    return result
recipes = ["tea", "omelette"]
ingredients =  [["milk", "caffeine", "sugar"], ["salt", "egg", "pepper"]] 
supplies = ["salt", "milk", "egg", "caffeine", "sugar"]
print(recipes2(recipes,ingredients,supplies))           