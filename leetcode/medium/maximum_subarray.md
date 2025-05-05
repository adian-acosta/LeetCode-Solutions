### Maximum Subarray (Forgot to start timer)
- Finding the subarray with the largest sum using Kadane's algorithm for a time complexity of O(n)
- The approach:
  1. Initialize a max sum to negative infinity and a current sum to 0
  2. While looping through the array compare the number being pointed at with our current sum added with the pointed number
  3. If our current sum plus the number is smaller than the pointed number itself then we can forget about everything before the pointer as there is a number(s) that hinder more than help back there, instead we'll set our current sum to the pointed number
  4. Continue along the array while comparing the current sum with the max sum and keeping track of the larger number
  5. Once we have gone through the array return the max sum
- This is a variation to the sliding window technique and can be used and improved upon for other problems such as if the indexes are needed instead. 
- It's a much more improved version compared to brute force method of using two pointers and tracking the sum with that leading to a time complexity of O(n^2)
- While i prefer this method there is another that is suppose to be more subtle in using the divide and conquer method, I'll try using that one soon but for now I prefer Kadane's algorithm for this problem