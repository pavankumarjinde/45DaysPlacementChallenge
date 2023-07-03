class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result=[]
        for i in range(len(nums)):
            x=target-nums[i]
            if x in nums[i+1:]:
                nums[i]=''
                result.extend([nums.index(x),i])
                break
        return result
