![alt text](image.png)

Comparison with the First Solution
First Solution (Naive Approach):

Uses direct string slicing and dictionary counts to find duplicates.
Time Complexity: O((N-k+1) * k), where N is the length of the string s and k is the window size. Each substring of length k is extracted and stored/checked.
Space Complexity: O((N-k+1) * k) due to storing each substring explicitly.
Second Solution (Rolling Hash):

Time Complexity: O(N), since each character is processed a constant number of times. The hash for each new window is computed in constant time using the previous hash.
Space Complexity: O(N-k+1), since at most, each window's hash and one instance of the substring are stored.
Advantages: More efficient for long strings with a relatively small alphabet (like DNA sequences with A, C, G, T).
Drawbacks: Slightly more complex due to managing the hashing and handling potential hash collisions (although actual collisions are rare with a well-chosen base and large dataset).


Overview of the Second Solution
The second solution uses a rolling hash technique to efficiently check for repeated sequences of length k in the string s. Here’s how it works:

Mapping Characters to Numbers: It converts each character in the string s to a number (e.g., 'A' to 1, 'C' to 2, etc.). This is useful for creating numerical hashes of substrings.

Initial Hash Calculation: For the first window of size k, it computes the hash value by treating the substring as a number in base-4 (considering A, C, G, T).

Rolling Hash: For subsequent substrings, it updates the hash in constant time. It removes the contribution of the first character of the previous window and adds the contribution of the new character at the end of the current window. This is done using:

hashing = (hashing - numbers[start - 1] * hi_place_value) * base + numbers[start + window_size - 1]
Where hi_place_value is the value of the highest place in a base-4 number of length k, allowing the algorithm to "slide" the window over by one position efficiently.
Checking for Duplicates: If a hash has been seen before, the corresponding substring is added to the result set output
