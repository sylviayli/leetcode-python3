# -*- coding:utf-8 -*-


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        temp_result = ""
        head_curr = 0
        tail_curr = len(s)
        curr = len(s)
        for i, letter in enumerate(s):
            head_curr = i

            for j, let in enumerate(s[::-1]):
                if s[head_curr] == let and i == j:
                    temp_result += letter
                    if len(temp_result) > len(result):
                        result = temp_result
                    temp_result = ""
                    break
                elif s[head_curr] == let and i != j:
                    temp_result += s[head_curr]
                    head_curr += 1

                elif s[head_curr] != let:
                    temp_result = ""
                    break
                if head_curr == len(s) or head_curr >= j:
                    print(temp_result)
                    temp_result = ""
                    break
            print(result)


so = Solution()
so.longestPalindrome("leetcode")

