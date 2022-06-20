# 13.Roman to Integer
# easy


class Solution:
    symbols = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInteger(self, s: str) -> int:
        result = 0

        for i in range(0, len(s)):
            index = i + 1
            current = self.symbols[f'{s[i]}']
            previus = self.symbols[f'{s[index]}']
            if current < previus:
                result += -current
            else:
                result += current

        return result
