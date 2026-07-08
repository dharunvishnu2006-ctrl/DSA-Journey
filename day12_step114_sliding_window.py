def max_sum_subarray(arr, k):
    """
    Find the maximum sum of any k consecutive elements in arr.

    Parameters:
        arr (list[int]): the input array of numbers
        k (int): the size of the sliding window

    Returns:
        int: the maximum sum found among all windows of size k

    Example:
        >>> max_sum_subarray([2, 1, 5, 1, 3, 2], 3)
        9
    """
    if len(arr) < k:
        return None  

    window_sum = sum(arr[:k])     
    max_sum = window_sum          

    for i in range(k, len(arr)):
        window_sum += arr[i]        
        window_sum -= arr[i - k]     
        max_sum = max(max_sum, window_sum)  
    return max_sum

def longest_unique_substring(s):
    """
    Find the length of the longest substring without repeating characters.

    Parameters:
        s (str): the input string

    Returns:
        int: length of the longest substring with all unique characters

    Example:
        >>> longest_unique_substring("abcabcbb")
        3
    """
    seen = set()          
    left = 0               
    max_len = 0            

    for right in range(len(s)):
        while s[right] in seen:          
            seen.remove(s[left])
            left += 1
        seen.add(s[right])              
        max_len = max(max_len, right - left + 1)   

    return max_len
from collections import Counter

def min_window_substring(s, t):
    """
    Find the smallest substring of s that contains all characters of t
    (including duplicates).

    Parameters:
        s (str): the string to search within
        t (str): the pattern whose characters must all be covered

    Returns:
        str: the smallest valid window, or "" if no valid window exists

    Example:
        >>> min_window_substring("ADOBECODEBANC", "ABC")
        'BANC'
    """
    if not s or not t:
        return ""

    need = Counter(t)          
    missing = len(t)           

    left = 0
    best_left, best_right = 0, float('inf')   
    for right, char in enumerate(s):
        if need[char] > 0:       
            missing -= 1
        need[char] -= 1           

        while missing == 0:        
            if right - left < best_right - best_left:
                best_left, best_right = left, right

            need[s[left]] += 1  
            if need[s[left]] > 0:      
                missing += 1
            left += 1                 

    return s[best_left:best_right + 1] if best_right != float('inf') else ""