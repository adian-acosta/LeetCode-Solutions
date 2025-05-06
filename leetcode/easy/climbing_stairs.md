### Climbing Stairs (Time Taken: 24 m 36 s)
- The easiest approach would be to use recursion since the nth stair can be reached from (n-1)th or (n-2)th, but a more optimized methods would be to use dynamic programming so we don't have to solve problems that have already been solved
- the approach (recursive):
    1. Set a base case if n = 0 or n = 1 then return 1 since that is the only possible solutions
    2. Make a recursive call for n-1 and n-2 for both the possible steps that can be taken and add both results together
    3. Return the sum of both recursive calls
- It is straight forward but has a time complexity of O(2^n) since we have to calculate the number of possible steps again of previously seen steps to get the current step
- The approach (dynamic programming):
    1. Create a sort of memo that will hold the solution of of previously seen steps with a size of n + 1 and all elements initialized to 0
    2. For the base case if n = 0 and n = 1, within the first two indexes set their values to be 1 since that is only possible number of steps able to be taken at those steps
    3. Iteratively loop starting at step 2 up till (n + 1)th step
    4. Calculate the possible number of steps by looking back at the previous two solutions and adding up their values then save the result into the memo at the current step
    5. Return the value in the memo at nth step
- This way allows us to save time by not having to calculate the answer of previously seen steps just to solve our current one giving us a time complexity of O(n)
- This approach does have a space complexity of O(n) but can be reduced down to O(1). Since we only care about the previous two subproblems, instead of creating a array to store those subproblems we can just have two variables hold the previous two solutions and use those