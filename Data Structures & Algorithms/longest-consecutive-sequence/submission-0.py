class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # HashSetにすることで重複排除できるのと、特定の値がデータに含まれているかを調べるのに平均O(1)しかかからない
        nums = set(nums)
        longest = 0

        for num in nums:
            if num-1 not in nums:
                length = 1
                while num + length in nums:
                    length += 1
                longest = max(longest, length)
            
        return longest