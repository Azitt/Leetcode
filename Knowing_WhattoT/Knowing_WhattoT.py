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