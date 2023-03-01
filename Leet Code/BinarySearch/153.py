#Find Minimum in Rotated Sorted Array
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        end = len(nums) - 1
        while left < end:
            mid = (left + end) // 2
            if nums[mid] > nums[end]:
                left = mid + 1
            else:
                end = mid
        return nums[left]