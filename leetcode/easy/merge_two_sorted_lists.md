### Merge Two Sorted List (Time taken: 53 m 0 s)
- Merging the two sorted list using both iteration and recursion for a time complexity of O(n + m)
- The approach (iteration):
  1. Create a dummy head with a temp that will move forward finding which value to add to the list
  2. Add a loop that will add on to temp while list1 **or** list2 are not at the end
  3. Compare the head of both list1 and list2 and which ever is the smallest value add that to temp, if both equal any could be picked
  3. Move the list that was chosen to add to temp forward then move temp forward also
  4. Repeat till one of the list is at the end then exit the loop
  5. If there is a list that is still not empty we can safetly assume that we can add the rest of that list on to temp while still being in the correct order since these list are already sorted
  6. Move the dummy head forward once then return dummy
- The approach (recursive):
  1. Setup a base case where if one of the list is empty then return the other one
  2. Compare the list for finding which one has the smallest first element to be returned at the end
  3. Move the list that was chosen foward by recursively calling the function with the inputs being the chosen list moved foward while the other remains unchanged
  4. Keep moving forward until either list is at their last element
- The iterative methods makes a lot more sense to me and it's the one I prefer. Struggled trying to grasp the recursive method as I had to look into solution for this one and while I understand it I don't yet have a full grasp of it yet.
