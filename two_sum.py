class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        #for i in range(len(nums)):
            #for j in range(i+1,len(nums)):
                #if nums[i]+nums[j] == target:
                    #return i,j
            #left = target - nums[i]
            #if left in nums and i!=nums.index(left):
                #return i, nums.index(left)
        for i,value in enumerate(nums):
            left = target - nums[i]
            if left in seen:
                return i,seen[left]  
            seen[value] = i
