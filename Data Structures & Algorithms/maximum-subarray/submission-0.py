class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum=-1
        sum1=0
        for i in range(len(nums)):
            sum1+=nums[i]
            if sum1>maxSum:
                maxSum=sum1
            if sum1<0:
                sum1=0
        return maxSum