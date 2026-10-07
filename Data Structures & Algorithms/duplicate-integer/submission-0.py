class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsMap = {}

        for num in nums:
            if numsMap.get(num) != None:
                return True
            numsMap[num] = num
        
        return False