def isValid(s):
    for i in range(len(s)): #done
        s = s.replace('()','')
        s = s.replace('[]','')
        s = s.replace('{}','')
        print(s)
        if s == '' :
            return True
    return False

"""""
    result from leetcode :
    Runtime: 40 ms, faster than 24.95% of Python3 online submissions for Valid Parentheses.
    Memory Usage: 14.4 MB, less than 7.96% of Python3 online submissions for Valid Parentheses.
"""""