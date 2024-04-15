def longest_repeating_character_replacement(s, k):
    string_length = len(s)
    length_of_max_substring = 0
    start = 0
    char_freq = {}
    most_freq_char = 0

    for end in range(string_length):
        if s[end] not in char_freq:
            char_freq[s[end]] = 1
        else:
            char_freq[s[end]] += 1

        most_freq_char = max(most_freq_char, char_freq[s[end]])

        if end - start + 1 - most_freq_char > k:
            char_freq[s[start]] -= 1
            start += 1
        
        length_of_max_substring = max(end - start + 1, length_of_max_substring)
        
    return length_of_max_substring  

if __name__ == '__main__':
   longest_repeating_character_replacement("aabccbb",2)                       