class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        curr = 0
        result = 0
        for i, tail in enumerate(s):
            if i == curr:
                continue

            if tail in s[curr:i]:
                result = i - curr if result < (i - curr) else result
                while i != curr:
                    curr += 1
                    if tail not in s[curr:i]:
                        result = i - curr if result < (i - curr) else result
                        break
            else:
                result = i - curr + 1 if result < (i - curr + 1) else result
                continue

        return result
