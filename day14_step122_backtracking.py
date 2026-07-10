def subsets(nums):
    result = []
    path = []
    
    def backtrack(start):
        result.append(path[:])          
        
        for i in range(start, len(nums)):
            path.append(nums[i])        
            backtrack(i + 1)            
            path.pop()                   
    
    backtrack(0)
    return result
nums = [1, 2, 3]
print(subsets(nums))

def permutations(nums):
    result = []
    path = []
    used = [False] * len(nums)
    
    def backtrack():
        if len(path) == len(nums):     
            result.append(path[:])
            return       
        for i in range(len(nums)):
            if used[i]:                 
                continue
            
            path.append(nums[i])      
            used[i] = True
            backtrack()              
            path.pop()                   
            used[i] = False                 
    backtrack()
    return result
nums = [1, 2, 3]
print(permutations(nums))

def combination_sum(nums, target):
    result = []
    path = []
    
    def backtrack(start, remaining):
        if remaining == 0:               
            result.append(path[:])
            return
        if remaining < 0:                  
            return
        
        for i in range(start, len(nums)):
            path.append(nums[i])          
            backtrack(i, remaining - nums[i])  
            path.pop()
    backtrack(0, target)
    return result
nums = [2, 3, 6, 7]
target = 7
print(combination_sum(nums, target))

def solve_n_queens(n):
    result = []
    cols = set()
    diag1 = set()   
    diag2 = set()   
    path = []       
    
    def backtrack(row):
        if row == n:
            result.append(path[:])                      
            return
        
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue                   
   
            path.append(col)
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            
            backtrack(row + 1)             
       
            path.pop()
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)
    
    backtrack(0)
    return result
solutions = solve_n_queens(4)
print(len(solutions))  
print(solutions)        