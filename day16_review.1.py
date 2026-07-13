def firstUniqueChar(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
    return -1

print(firstUniqueChar("leetcode"))      
print(firstUniqueChar("loveleetcode"))  
print(firstUniqueChar("aabb"))          
print(firstUniqueChar("abcabcde"))