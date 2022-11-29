"""
Write a function that given a roman numeral it will convert it to an integer.

Solution:
Runtime 113 ms
Memory 13.9 MB 
"""
def romanToInt(self, s: str) -> int:
    sum = 0
    
    for ele, letter in enumerate(s):
        if ele != len(s) - 1:
            if s[ele] == 'I' and (s[ele+1] == 'V' or s[ele+1] == 'X'):
                sum -= 1
                continue
            if s[ele] == 'X' and (s[ele+1] == 'L' or s[ele+1] == 'C'):
                sum -= 10
                continue
            if s[ele] == 'C' and (s[ele+1] == 'D' or s[ele+1] == 'M'):
                sum -= 100
                continue
        
        if s[ele] == 'I':
            sum += 1
        
        if s[ele] == 'V':
            sum += 5
        
        if s[ele] == 'X':
            sum += 10
        
        if s[ele] == 'L':
            sum += 50
        
        if s[ele] == 'C':
            sum += 100
        
        if s[ele] == 'D':
            sum += 500
        
        if s[ele] == 'M':
            sum += 1000
    return sum

