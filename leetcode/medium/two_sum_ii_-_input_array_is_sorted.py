class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]: # type: ignore
        # binary search solution
        
        for i in range(len(numbers)):
            # searching the right of the left element in case of duplicate answers
            left = i + 1
            right = len(numbers) - 1
            
            while left <= right:
                mid = left + (right - left) // 2
                # think of it as numbers[i] is left and numbers[mid] is right
                if target - numbers[i] == numbers[mid]:
                    return [i + 1, mid + 1]
                elif target - numbers[i] > numbers[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        # no solution was found
        return []
        
        
        # two pointer solution
        
        # # set up both left and right pointers
        # left = 0
        # right = len(numbers) - 1
        
        # # loop while the two pointers are not equal or have not past each other
        # while left < right:
        #     # compare the two elements, if they are equal to our target return the pointers index + 1
        #     if numbers[left] + numbers[right] == target:
        #         return [left + 1, right + 1]
            
        #     # if the complement of the target - right pointer is greater than left pointer then we shift left pointer forward, otherwise shift right pointer backwards
        #     if target - numbers[right] > numbers[left]:
        #         left += 1
        #     else:
        #         right -= 1
        
        # # no solution was found
        # return [left + 1, right + 1]