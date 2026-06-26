def frequency_count(arr):
    freq = {}                          
    for item in arr:                   
        freq[item] = freq.get(item, 0) + 1  
    return freq
ip_logs = ["192.168.1.1", "10.0.0.1", "192.168.1.1", 
           "172.16.0.1", "10.0.0.1", "192.168.1.1"]

result = frequency_count(ip_logs)
print(result)
most_frequent = max(result, key=result.get)
print(most_frequent)

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):     
        complement = target - num        
        if complement in seen:         
            return [seen[complement], i] 
        seen[num] = i                 
    return []                        

print(two_sum([2, 7, 11, 15], 9))  
print(two_sum([3, 2, 4], 6))         
print(two_sum([3, 3], 6))           

def first_unique_character(s):
    freq = {}                           

    for char in s:                      
        freq[char] = freq.get(char, 0) + 1 

    for i, char in enumerate(s):        
        if freq[char] == 1:             
            return i              

    return -1                           
print(first_unique_character("leetcode"))     
print(first_unique_character("loveleetcode"))
print(first_unique_character("aabb"))        
log = "errorwarningerrorinfo"
idx = first_unique_character(log)
print(f"First unique character in log: '{log[idx]}' at index {idx}")