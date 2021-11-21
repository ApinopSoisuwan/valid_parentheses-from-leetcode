def isValid(s):
    for i in range(len(s)//2): #done #reduce loop
        s = s.replace('()','')
        s = s.replace('[]','')
        s = s.replace('{}','')
        print(s)
        if s == '' :
            return True
    return False


"""""
result from leetcode :
Runtime: 44 ms, faster than 20.22% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14.2 MB, less than 65.38% of Python3 online submissions for Valid Parentheses.
"""""