# https://leetcode.com/problems/string-to-integer-atoi/submissions/
from re import match

MAX = 2 ** 31
MIN = -MAX
VALID = {*'0123456789-+'}


class Solution:
    def myAtoi(self, value: str) -> int:
        m = match(r'[+-]?\d+', value.strip())
        if not m:
            return 0
        n = int(m[0])
        return min(MAX - 1, max(MIN, n))


print(Solution().myAtoi('-999999999999999999999'))
