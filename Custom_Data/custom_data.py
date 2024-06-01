## Snapshot Array ################
class Snapshot_array:
    def __init__(self,length):
        self.length = length
        self.array = [0]*length
        self.snapshot = []
        self.snapID= 0
    def value(self,idx,val):
        if idx < self.length:
            self.array[idx] = val
    def Snapshot(self):
        snapID = len(self.snapshot)
        self.snapshot.append(self.array.copy())
        return snapID 
    
    def Get_value(self,idx,snapID):
           return self.snapshot[snapID][idx]
## better solution##################
import copy
class Snapshot_array:
    def __init__(self,length):
        self.length = length
        self.array = dict()
        self.array[0] = dict()
        self.snapID= 0
    def value(self,idx,val):
        if idx < self.length:
            self.array[self.snapID][idx] = val
    def Snapshot(self):
        # print("self.array1",self.array)
        self.array[self.snapID+1] =copy.deepcopy(self.array[self.snapID])
        # print("self.snapped",self.array)
        self.snapID += 1
        return self.snapID -1 
    
    def Get_value(self,idx,snapID):
        #    print(self.array)
           if snapID < self.snapID and snapID >= 0 and idx < self.length:
               return self.array[snapID][idx] if idx in self.array[snapID] else 0
           else:
               return None           
num_nodes = 3
node_values = [[0, 5], [0, 1], [2, 3], [1, 10]] 
values_to_get = [[0, 0], [0, 1], [1, 0]]  
snapshot_arr = Snapshot_array(num_nodes) 
for j in node_values:
    snapshot_arr.value(j[0],j[1])
    snapshot_arr.Snapshot()    
for j in values_to_get:
    print(snapshot_arr.Get_value(j[0],j[1])) 

### Time-Based Key-Value Store ############ 
import random
class time_basedKV:
    def __init__(self):
        self.value_dict = {}
        self.timestamp_dict = {}
    def set_value(self,key , value ,timestamp):
        if key in self.value_dict:
            if value != self.value_dict[key][-1]:
                self.value_dict[key].append(value)
                self.timestamp_dict[key].append(timestamp)
        else:
           self.value_dict[key] = [value]
           self.timestamp_dict[key] = [timestamp]
                    
    def get_value(self,key,timestamp):
        
        if key not in self.timestamp_dict:
            return ""
        
        timestamps = self.timestamp_dict[key]
        left = 0
        right = len(timestamps)-1
        ans = -1
        while left <= right:
            mid = left + (right - left)//2
            if timestamps[mid] <= timestamp:
                ans = mid
                left = mid + 1
            else:
                right = mid -1   
        return self.value_dict[key][ans] if ans != -1 else "" 
def main():
    ts = time_basedKV()
    num = 1
    random_value = 0
    input = (
            ("course", "OOP", 3),
            ("course", "PF", 5),
            ("course", "OS", 7),
            ("course", "ALGO", 9),
            ("course", "DB", 10)
        )
    for i in input:
        ts.set_value(i[0], i[1], i[2])
        random_value = random.randint(0, 10)
        print(random_value)
        print(ts.get_value("course", random_value))
        num += 1

if __name__ == "__main__":
    main()  
    
## Implement LRU Cache ####################
from linked_list import LinkedList

class LRU_chace:
    def __init__(self,capacity):
        self.capacity = capacity 
        self.cache_map = {}
        self.cache_list = LinkedList() 
    def set(self,key,value):
        if key in self.cache_map:
            found_iter = self.cache_map[key]
            self.cache_list.move_to_head(found_iter)
            found_iter.pair[1] = value
            return
        if len(self.cache_map) == self.capacity:
            key_tmp = self.cache_list.get_tail().pair[0]
            self.cache_list.remove_tail()
            del self.cache_map[key_tmp]
                    
        self.cache_list.insert_at_head([key,value]) 
        self.cache_map[key] = self.cache_list.get_head()
           
    def get(self,key):
        found_iter = None
        if key in self.cache_map:
            found_iter= self.cache_map[key]
        else:
            return -1  
        list_iterator = found_iter
        self.cache_list.move_to_head(found_iter)
        
        return list_iterator.pair[1]      
                
capacity = 2
cache = LRU_chace(capacity)
keys = [10, 10, 15, 20, 15, 25, 5]
values = ["20", "get", "25", "40", "get", "85", "5"] 
for i in range(len(keys)):
        if values[i] == "get":
            print("Getting by Key: ", keys[i])
            print("Cached value returned: ", cache.get(keys[i]))
        else:
            print("Setting cache: Key: ", keys[i], ", Value: ", values[i])
            cache.set(keys[i], int(values[i]))                           

## Insert Delete GetRandom #####################
from random import choice

class RandomSet():
       def __init__(self):
         self.array = []
         self.hash_map ={}
         
       def insert(self,data):
            if data in self.hash_map:
                return False
            else:
                self.hash_map[data] = len(self.array)
                self.array.append(data)
                return True
       def delete(self,data):  
           if data in self.hash_map:
               index = self.hash_map[data]
               last_in_array = self.array[-1]
               self.array[index], self.array[-1],self.hash_map[last_in_array] = last_in_array, data,i
               del self.hash_map[data] # del just work for hash_map (dictionary) not array 
               self.array.pop()
               return True
           return False
       def get_random(self):
            return choice(self.store)             
                        
commands = [["I", "I", "I", "R", "R", "G"],
                ["I", "I", "R", "G", "R", "I"]]
values = [[10, -1, 100, 10, 200, -1], [30, 60, 10, -1, 30, 90]]

for i in range(len(commands)):
        dataset = RandomSet()
        print(i + 1, ". Starting operations:", "\n", sep="")

        for j in range(len(commands[i])):
            if commands[i][j] == "I":
                print("\tInsert (", values[i][j], ") returns ",
                      dataset.insert(values[i][j]), sep="")
            elif commands[i][j] == "R":
                print("\tDelete (", values[i][j], ") returns ",
                      dataset.delete(values[i][j]), sep="") 
                break
        print(dataset.array,dataset.hash_map)  
## min stack ###################################### 

class MinStack():
      def __init__(self):
          self.min_stack = []
          self.main_stack = [] 
      def push(self,data):
          self.main_stack.append(data)

          if  len(self.min_stack) == 0 or (data < self.min_stack[-1]):
              self.min_stack.append(data)
          else:
              self.min_stack.append(self.min_stack[-1]) 
      def pop(self):
          self.min_stack.pop()
          return self.main_stack.pop()
      def min_number(self):
          if len(self.min_stack) != 0:
              return self.min_stack[-1]                                                   

data = [9, 3, 1, 4, 2, 5]          
commands = ["I", "I", "I", "min", "R", "G"]
min_stack = MinStack()
for j in range(len(commands)):
            if commands[j] == "I":
                print("\tInsert (", data[j], ") returns ",
                      min_stack.push(data[j]), sep="")
            elif commands[j] == "min":
                # print("\tDelete (", values[i][j], ") returns ",
                      print(min_stack.min_number())

print(min_stack.min_stack,min_stack.main_stack)

## LFU Cache #######################################
class LFUCache():
    
    def __init__(self,capacity):
        self.capacity = capacity
        self.lfu_cache = {}
        self.freq_count = {}
    def put(self,key,value):
        if key in self.lfu_cache:
            self.freq_count[key] += 1
            return
        if len(self.lfu_cache) == self.capacity: 
            min_freq = min(self.freq_count.values())
            for k,v in self.freq_count.items():
                if v == min_freq:
                    key = k
            del self.lfu_cache[key]
            del self.freq_count[key]
            
        self.lfu_cache[key] = value
        self.freq_count[key] = 1               
    def get(self,key):                          