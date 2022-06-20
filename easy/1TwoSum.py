# 1.Two Sum
# easy
# autor: Alison Dev


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        listIndexes = []

        for indx, number in enumerate(nums):
            x = target - number

            if x in nums and indx != nums.index(x):
                listIndexes.append(indx)
                listIndexes.append(nums.index(x))

                return listIndexes


solution = Solution()
print(solution.twoSum([3, 3], 6))
