class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        while l < r:
            # 整数オーバーフローを防ぐ安全な書き方
            mid = l + (r-l) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
            
        return nums[l]