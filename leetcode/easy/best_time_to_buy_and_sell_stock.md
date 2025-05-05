### Best Time to Buy and Sell Stock (Time taken: 17 m 19 s)
- Using the [sliding window](https://www.geeksforgeeks.org/window-sliding-technique/) technique with an aim for that time complexity of O(n).
- The approach:
  1. Keep track of the lowest price seen so far.
  2. At each step calculate profit = current price - lowest price
  3. If the calculated profit is higher than our current max profit update it to be our new max profit
  4. Time complexity of O(n) because we only pass once through the list
- after finding the answer and submitting I reviewed other's solutions, while identical in approach my code can be much more clearer and with minor optimizing such as instead of r starting at index 0 it should start at index 1. Instead of the variables being indexes they should be the elements themselves this would make the code much more cleaner and easier to understand.
- Struggled at first in putting the idea into practice but after drawing it out in ms paint it became much more clearer, I will have to get in the habit of drawing out the problems more often.