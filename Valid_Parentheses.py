class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        for char in s:
            if char in ['{','[','(']:
                stack.append(char)
            else:
                if not stack:
                    return False
                cur_char = stack.pop()
                if cur_char =='(':
                    if char != ')':
                        return False
                if cur_char =='[':
                    if char != ']':
                        return False
                if cur_char =='{':
                    if char != '}':
                        return False
        if stack :
            return False
        return True
