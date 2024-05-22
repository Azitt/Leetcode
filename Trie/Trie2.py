class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_string = False
class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        node = self.root        
        for c in word:
            if c not in node.children:
                 node.children[c] = TrieNode()
            node = node.children[c]
        node.is_string = True 
    # Function to search a string from the trie
    def search(self, string_to_search):
        node = self.root
        for c in string_to_search:
            if c not in node.children:
                return False
            node = node.children.get(c)
        return node.is_string
    
    # Function to search prefix of strings
    def starts_with(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children.get(c)
        return True

    # Function to delete the characters in the searched word that are not shared
    def remove_characters(self, string_to_delete):
        node = self.root
        child_list = []
    
        for c in string_to_delete:
            child_list.append([node, c])
            node = node.children[c]
        
        for pair in reversed(child_list):
            parent = pair[0]
            child_char = pair[1]
            target = parent.children[child_char]

            if target.children:
                return
            del parent.children[child_char]
    def preorder(self, node, path, result):
        if node.is_string:
            result.append(int("".join(path)))
        for digit in sorted(node.children.keys()):
            path.append(digit)
            self.preorder(node.children[digit], path, result)
            path.pop()  # backtrack        

## Word Search II ########################                   
def find_strings(grid,words):
    trie_for_words = Trie()
    result = []
    for w in words:
        trie_for_words.insert(w)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            dfs(trie_for_words,trie_for_words.root,grid,i,j,result,'')
    return result

def dfs(words_trie,node,grid,row,col,result,word):
    if node.is_string:
        result.append(word)
        node.is_string = False
        words_trie.remove_characters(word)
    
    if 0<= row< len(grid) and 0<= col<len(grid[0]):
        char= grid[row][col]
        child = node.children.get(char)        
        if child is not None:
            word += char
            grid[row][col] = None
            for row_offset,col_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dfs(words_trie,child,grid,row+row_offset,col+col_offset,result,word) 
            grid[row][col] = char                   
                
test_case_grid = [['B', 'S', 'L', 'I', 'M'], 
                  ['R', 'I', 'L', 'M', 'O'], 
                  ['O', 'L', 'I', 'E', 'O'], 
                  ['R', 'Y', 'I', 'L', 'N'], 
                  ['B', 'U', 'N', 'E', 'C']] 

strings_to_search = ["BUY", "SLICK", "SLIME", "ONLINE", "NOW"] 
print(find_strings(test_case_grid, strings_to_search))

## Lexicographical Numbers #########################
def lexicographical_order(n):
    t = Trie()
    for i in range(1,n+1):
        t.insert(str(i))
    result = []
    t.preorder(t.root,[],result)
    return result

print(lexicographical_order(13))                          