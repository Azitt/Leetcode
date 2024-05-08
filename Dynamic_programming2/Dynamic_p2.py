 
def word_break2(s,word_dict):
    def backtrack(prefix,suffix):
     if not suffix:
        return [prefix]
     result = []
     for word in word_dict:
        if suffix.startswith(word):
            result.extend(backtrack(prefix+[word],suffix[len(word):]))
     return result       
            
    return backtrack([],s) 

s = "catsanddog"
word_dict = ["cat", "cats", "and", "sand", "dog"]
print(word_break2(s, word_dict))

def word_break2(s, word_dict):
    dp = [[]] * (len(s) + 1)
    dp[0] = [""]

    for i in range(1, len(s) + 1):

        prefix = s[:i]

        temp = []

        for j in range(0, i):
            suffix = prefix[j:]
            
            if suffix in word_dict:
                
                for substring in dp[j]:
                    temp.append((substring + " " + suffix).strip())

        dp[i] = temp

    return dp[len(s)]
s = "catsanddog"
word_dict = ["cat", "cats", "and", "sand", "dog"]
print(word_break2(s, word_dict))


                 