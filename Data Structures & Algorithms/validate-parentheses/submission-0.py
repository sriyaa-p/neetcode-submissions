class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }   
        for p in s:
            if p in "({[":
                stack.append(p)
            else:
                if not stack or stack.pop()!=pairs[p]:
                    return False
        return len(stack)==0