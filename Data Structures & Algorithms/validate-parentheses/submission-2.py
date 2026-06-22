class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ')' : '(',
            '}' : '{',
            ']' : '[',
        }

        stack = []

        for char in s:
            if char not in mapping:
                stack.append(char)
            
            else:
                if not stack:
                    return False
                    
                if stack[-1] != mapping[char]:
                    return False

                stack.pop()

        if stack:
            return False

        return True

        