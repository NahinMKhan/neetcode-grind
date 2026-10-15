class Solution:
    def isValid(self, s: str) -> bool:
        hash = {'}':'{', ']':'[', ')':'('}
        stack = []
        for c in s:
            if c in hash: #checks if open parentheses
                if stack and stack[-1] == hash[c]: #if open parentheses and top of stack match then pop
                    stack.pop()
                else: #not match so false
                    return False
            else: #if closed parentheses
                stack.append(c)
        return True if not stack else False #if stack is empty then true else false
        