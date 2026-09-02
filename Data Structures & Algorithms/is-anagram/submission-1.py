class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # The Len of the strings and The characters should be same
        if len(s)!=len(t):
            return False
        hashmap={}
        for i,char in enumerate(s):
            hashmap[char]=hashmap.get(char,0)+1
        for char in t:
            if char not in hashmap:
                return False
            hashmap[char]-=1
            if hashmap[char]<0:
                return False
        return True