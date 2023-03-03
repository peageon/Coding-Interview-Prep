#Search in Rotated Sorted Array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[right]:
                if nums[mid] < target:
                    left = mid + 1
                else:
                    if target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
            else:
                if nums[mid] < target:
                    if nums[right] < target:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    right = mid - 1
        
        if nums[right] != target:
            return -1
        return right
