class Solution:
    def climbStairs(self, n: int) -> int:
        # create an array the size of n with all elements set to 0
        steps = [0] * (n + 1)

        # base cases, if n = 0 do nothing stay on the ground if n = 1 can only take 1 step
        steps[0] = 1
        steps[1] = 1

        # start off at the second step since the first two are already solved
        for i in range(2, n + 1):
            # the previous two steps already have a solution, look back and add them to get the next sum then save it in the array 
            steps[i] = steps[i - 1] + steps[i - 2]
        
        # return the last index of the array as it holds the solution to the nth step
        return steps[n]

        # if n == 0 or n == 1:
        #     return 1
        
        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)