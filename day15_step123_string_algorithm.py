def build_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0      
    i = 1  
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]  
            else:
                lps[i] = 0
                i += 1    
    return lps

def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    lps = build_lps(pattern)
    result = []
    
    i = j = 0  
    
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == m:                 
                result.append(i - j)    
                j = lps[j - 1]          
        else:
            if j != 0:
                j = lps[j - 1]         
            else:
                i += 1   
    return result
text = "AAAAABAAABA"
pattern = "AAAB"
print(kmp_search(text, pattern))   

def naive_search(text, pattern):
    n, m = len(text), len(pattern)
    result = []
    
    for i in range(n - m + 1):   
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:                 
            result.append(i)  
    return result
text = "AAAAABAAABA"
pattern = "AAAB"
print(naive_search(text, pattern))

def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    if m > n:
        return []
    
    base = 256
    mod = 10**9 + 7
    result = []    
    pattern_hash = 0
    window_hash = 0
    h = 1                    
    
    for i in range(m - 1):
        h = (h * base) % mod
    
    for i in range(m):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % mod
        window_hash = (window_hash * base + ord(text[i])) % mod
    
    for i in range(n - m + 1):
        if pattern_hash == window_hash:       
            if text[i:i+m] == pattern:
                result.append(i)       
        if i < n - m:                          
            window_hash = (window_hash - ord(text[i]) * h) % mod
            window_hash = (window_hash * base + ord(text[i + m])) % mod
            window_hash = window_hash % mod
    
    return result
text = "AAAAABAAABA"
pattern = "AAAB"
print(rabin_karp(text, pattern))