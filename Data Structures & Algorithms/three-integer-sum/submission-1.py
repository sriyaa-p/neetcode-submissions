class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        # check if the value is duplicate 
        for i,num in enumerate(nums):
            if i>0 and num==nums[i-1]:
                continue
            # using two pointer method
            # left = i+1 because we have already seen i=0, so start with the next value
            left,right=i+1, len(nums)-1
            while left<right:
                threeSum=num+nums[left]+nums[right]
                if threeSum>0:
                    right-=1
                elif threeSum<0:
                    left+=1
                else:
                    # threeSum=0
                    result.append([num, nums[left],nums[right]])
                    left+=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
        return result