def count_set_bits(n):
    count = 0
    while n:
        n &= (n - 1)   
        count += 1
    return count

def single_number(nums):
    result = 0
    for num in nums:
        result^= num
    return result    

def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0