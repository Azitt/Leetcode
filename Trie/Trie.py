class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_word = False

## Implement Trie #################
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self,word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children.get(c)    
        # set the boolean variable to TRUE for the corresponding node
        node.is_word = True
    def search(self,word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children.get(c)
        return node.is_word
    def search_prefix(self,prefix):    
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children.get(c)
        return True

word = "there" 
trie_for_keys = Trie()
trie_for_keys.insert(word)
print(trie_for_keys.search("xyn"))
print(trie_for_keys.search_prefix("the"))   

## Search Suggestions System ################
class TrieNode2:
    def __init__(self):
        self.search_words = []
        self.children = {}
        
class Trie2:
    def __init__(self):
        self.root = TrieNode2()
        
    def insert(self,word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode2()
            node = node.children.get(c) 
            if len(node.search_words)< 3: ## 3 here because question said return three suggestion#################
                node.search_words.append(word)
              
                
    def search(self,word):
        node = self.root
        result = []
        for i, c in enumerate(word):
            if c not in node.children: 
                temp = [[] for _ in range(len(word) - i)]  
                return result + temp
            else:
                node = node.children[c]
                result.append(node.search_words[:]) 
        return result  
def suggested_products(products,search_word):
    products.sort()
    trie = Trie2()
    for p in products:
        trie.insert(p)
    return trie.search(search_word)    
        
                    
products = ["bat", "bag", "bassinet", "bread", "cable",
                "table", "tree", "tarp"]
search_word_list = "ba" 
print(suggested_products(products,search_word_list))

## Replace Words ####################################
class TrieNode3:
    def __init__(self):
        self.end_of_word = False
        self.children = {}                
class Trie3:
    def __init__(self):
        self.root = TrieNode3()
    
    def insert(self,word):
        node = self.root
        
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode3()            
            node = node.children.get(c)
        node.end_of_word = True
    def replace(self,sentence):
        words = sentence.split()
        for i,w in enumerate(words):
            node = self.root
            for j,c in enumerate(w):
              if c not in node.children:
                break  
              node = node.children.get(c)
              if node.end_of_word:
                 words[i] = w[:j+1] 
                 print(words[i])
                 break
        return ' '.join(words)      

sentence,dictionary = "where there is a will there is a way" , ["wi","wa","w"]
trie = Trie3()
for d in dictionary:
 trie.insert(d)
print(trie.replace(sentence)) 


            
              
                                 