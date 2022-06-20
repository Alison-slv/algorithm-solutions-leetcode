# problem: 1480 Running Sum Of 1d Array
# difficulty: easy
# ---------------------------------------
# Given an array nums.
# We define a running sum of an array as:
# runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        numsList = []
        numsSum = 0

        for i in nums:
            numsList.append(numsSum + i)
            numsSum += i

        return numsList

listNums = [3, 1, 2, 10, 1]
print(Solution().runningSum(listNums))
