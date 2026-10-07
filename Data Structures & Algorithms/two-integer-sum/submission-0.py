class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}

        for i, num in enumerate(nums):
            targetNum = target - num

            if numsMap.get(targetNum) != None:
                return [numsMap.get(targetNum), i]

            numsMap[num] = i

        return []