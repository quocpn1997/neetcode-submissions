class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}

        for i, num in enumerate(nums):
            targetNum = target - num

            numFromMap = numsMap.get(targetNum)
            if numFromMap != None:
                return [numFromMap, i]

            numsMap[num] = i

        return []