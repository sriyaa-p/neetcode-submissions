class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # target = num + complement, so complement = target-num
        hash_map={} # An empty dictionary to store the visited values
        for i,num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return [hash_map[complement],i]
            hash_map[num]=i
        return []