### Two Sum (Time taken: 5 m 40 s)

- Instead of using a brute force method to check every pair of elements (which would be too slow), I chose to use a hashmap to make the code more efficient.
- The approach:
  1. For each element, find the complement of the target by subtracting the current element.
  2. Check if the complement exists in the hashmap.
  3. If the complement is not in the hashmap, add the current element and its index to the hashmap.
  4. If the complement is found, return both its index and the index of the current element.
- This reduces the time complexity because we can return early when the solution is found, avoiding the need to iterate through the entire list. The worst-case scenario is when the solution is at the very end.