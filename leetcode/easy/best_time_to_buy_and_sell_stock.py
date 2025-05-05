class Solution:
    def maxProfit(self, prices: List[int]) -> int: # type: ignore
        l = 0
        profit = 0
        n = len(prices)

        # shifts the window throughout the array
        for r in range(n):
            # looking for the lowest price possible
            if prices[r] < prices[l]:
                l = r
            
            # if a profit is able to be made then buy
            profit = max(prices[r] - prices[l], profit)   
        
        # if any profit was made then return the result, if there is no profit then return 0
        return profit