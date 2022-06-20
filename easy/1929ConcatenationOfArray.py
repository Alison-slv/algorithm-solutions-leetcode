# problem: 1929 Concatenation Of Array
# difficulty: Easy


class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums * 2


print(Solution().getConcatenation([1, 2, 3]))


# input  > [1, 2, 3]
# output > [1, 2, 3, 1, 2, 3]
