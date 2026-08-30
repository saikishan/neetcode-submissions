class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        k, i, j = 0, 0, 0
        result = list()
        for k in range(len(nums)-2):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            
            i, j =  k + 1, len(nums) - 1

            while i < j:
                total = nums[k] + nums[i] + nums[j]
                if total < 0:
                    i += 1
                elif total > 0:
                    j -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    while i < j and nums[i] == nums[i+1]:
                        i += 1
                    i+=1
                
        return result
