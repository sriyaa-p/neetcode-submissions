class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Brute Force method and Time Complexity is O(N^2)
        '''
        n=len(s)
        maxlen=0
        for i in range(n):
            hashmap=[0]*256
            for j in range(i,n):
                if (hashmap[ord(s[j])]==1):
                    break
                length=j-i+1
                maxlen= max(length,maxlen)
                hashmap[ord(s[j])]=1
        return maxlen
        '''
        left,right=0,0 #start at the 0th index
        maxlength=0 #initially the maximum length is zero
        n=len(s)
        hashmap={}
        while right<n:
            if s[right] in hashmap :
                if hashmap[s[right]]>=left:
                    left=hashmap[s[right]]+1
            length=right-left+1
            maxlength=max(length,maxlength)
            hashmap[s[right]]=right
            right+=1
        return maxlength