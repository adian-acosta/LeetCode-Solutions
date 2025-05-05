class Solution:
    def maxSubArray(self, nums: List[int]) -> int: # type: ignore
        # This is a solution using Kadane's algorithm
        max_sum = 0
        curr_sum = 0

        for num in nums:
            # if our current sum added with the pointed num is smaller than the num itself, we can forget
            # about anything before that pointer as it doesn't help anymore and set the current sum to num.
            curr_sum = max(curr_sum + num, num)
            max_sum = max(curr_sum, max_sum)
        
        return max_sum