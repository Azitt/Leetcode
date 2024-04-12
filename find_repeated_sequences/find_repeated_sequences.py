def find_repeated_sequences(s, k):
    hash_map = {}
    result = []
    for i in range(len(s) - k + 1):  # Ensure we only consider valid full-length substrings
        current_sub = s[i:i+k]
        hash_map[current_sub] = hash_map.get(current_sub, 0) + 1
        if hash_map[current_sub] == 2:
            result.append(current_sub)
    return result


def find_repeated_sequences(s, k):
    window_size = k
    if len(s) <= window_size:
        return set()
    base = 4
    hi_place_value = pow(base, window_size - 1)
    mapping = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    numbers = []
    for i in range(len(s)):
        numbers.append(mapping.get(s[i]))
    hashing = 0
    substring_hashes, output = set(), set()
    for start in range(len(s) - window_size + 1):
        if start != 0:
            hashing = (hashing - numbers[start - 1] * hi_place_value) * base \
                + numbers[start + window_size - 1]
        else:
            for end in range(window_size):
                hashing = hashing * base + numbers[end]
        if hashing in substring_hashes:
            output.add(s[start:start + window_size])
        substring_hashes.add(hashing)
    return output


