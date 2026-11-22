class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d1={}
        for i in range(0,len(nums)):
            x=target-nums[i]
            if x in d1:
                return [i,d1[x]]
            else :
                d1[nums[i]]=i

        