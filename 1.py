class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 暴力法 这个答案超时了
        #         for i, first in enumerate(nums):
        #             for j, second in enumerate(nums):
        #                 if i == j:
        #                     continue
        #                 if (first + second) == target:
        #                     return [i, j]

        #         return []
        num_dict = {}
        for i, num in enumerate(nums):
            num_dict[str(num)] = i
        print(num_dict)

        for i, num in enumerate(nums):
            if num_dict.__contains__(str(target - num)):
                if i == int(num_dict[str(target - num)]):
                    continue
                return [i, int(num_dict[str(target - num)])]

        return []
