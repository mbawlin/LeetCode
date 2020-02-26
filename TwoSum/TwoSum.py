class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #target-nums[1]-> dict (n)
        #dict [x,y,z] (1)
        #if nums[i] -> dict (n)
        #bin output, store index
        diff = {}
        out = []
                                                                            
        for i in range(len(nums)): ##range for index not element
            if (target - nums[i] not in diff):
                diff[nums[i]] = i #diff = {2,0, etc}
            else: 
                out = [diff[target-nums[i]],i]
                return out
        return out



