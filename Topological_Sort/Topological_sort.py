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