# problem: 1290 Build Array From Permutation
# dificulty: easy


class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans = []

        for i in nums:
            ans.append(nums[i])

        return ans





print(Solution().buildArray([0, 2, 1, 5, 3, 4]))

# input  > [0, 2, 1, 5, 3, 4]
# output > [0, 1, 2, 4, 5, 3]
