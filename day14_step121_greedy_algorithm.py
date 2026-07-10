def activity_selection(activities):
    activities.sort(key=lambda x: x[1])   
    count = 1
    last_end = activities[0][1]
    
    for i in range(1, len(activities)):
        start, end = activities[i]
        if start >= last_end:             
            count += 1
            last_end = end
    return count

activities = [(1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10), (8,11), (8,12), (2,14), (12,16)]
print(activity_selection(activities))  

def can_jump(nums):
    farthest = 0
    
    for i in range(len(nums)):
        if i > farthest:          
            return False
        farthest = max(farthest, i + nums[i])
    
    return True
nums = [2, 3, 1, 1, 4]
print(can_jump(nums)) 
nums2 = [3, 2, 1, 0, 4]
print(can_jump(nums2))  

def can_complete_circuit(gas, cost):
    total_tank = 0
    curr_tank = 0
    start = 0
    
    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total_tank += diff
        curr_tank += diff
        
        if curr_tank < 0:          
            start = i + 1          
            curr_tank = 0
    
    return start if total_tank >= 0 else -1
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(can_complete_circuit(gas, cost))  

def find_content_children(g, s):
    g.sort()             
    s.sort()           
    child = 0
    cookie = 0
    
    while child < len(g) and cookie < len(s):
        if s[cookie] >= g[child]:      
            child += 1                
        cookie += 1                   
    return child
g = [1, 2, 3]
s = [1, 1]
print(find_content_children(g, s))  