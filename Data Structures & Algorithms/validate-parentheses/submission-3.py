class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []

        for i in range(0, len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else:
                if (len(stack) == 0):
                    return False
                top = stack.pop()
                if not self.isMatch(top, s[i]):
                    return False
        
        if len(stack) == 0:
            return True
        
        return False
        
    

    def isMatch(self, s1: str, s2: str) -> bool:
        if (s1 == '(' and s2 == ')') or (s1 == '{' and s2 == '}') or (s1 == '[' and s2 == ']'):
            return True
        else:
            return False

# if an open bracket push onto stack
# if come across a close bracket pop stack and check if it matches with curr brace

        