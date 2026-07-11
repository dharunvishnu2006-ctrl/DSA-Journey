def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))

def reverse_string(s):
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

s = ['h', 'e', 'l', 'l', 'o']
reverse_string(s)
print(s)

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in t:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] < 0:
            return False
    return True

s = "anagram"
t = "nagaram"
print(is_anagram(s, t))

s2 = "rat"
t2 = "car"
print(is_anagram(s2, t2))

def fizz_buzz(n):
    result = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))

    return result
n = 15
print(fizz_buzz(n))

def is_palindrome(x):
    if x < 0:
        return False

    original = x
    reversed_num = 0

    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10

    return original == reversed_num

x = 121
print(is_palindrome(x))  
x2 = -121
print(is_palindrome(x2))  
x3 = 10
print(is_palindrome(x3)) 