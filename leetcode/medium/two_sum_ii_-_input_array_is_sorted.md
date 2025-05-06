### Two Sum II - Input Array Is Sorted (Time Taken: 3 m 49 s)
- Initially solved the program using a two pointer approach, but since I finished the problem too quickly i decided to also try out using binary search since the array is already sorted
- The approach (two pointers):
    1. Initalize two pointers, one to the left of the array and another to the right of the array
    2. Loop through the array while both pointers have not past each other or are not equal to each other
    3. Check if both pointers added together is equal to our target if so then return the pointers index + 1
    4. If the complement of target minus our right element is greater than the left element then move the left pointer forward, otherwise move the right pointer backwards
- It's a more straight forward approach with a time complexity of O(n) 
- The approach (binary search):
    1. Set up an outer loop that will move the left pointer forward if the inner loop does not find a solution
    2. Set up two pointers left and right with having the left equal to the count of the outer loop plus 1 since we wanna search the right of the left element in the case of there being duplicate answers.
    3. Find the middle index between the left and right pointers
    3. If the target minus the element equal to the count of the outer loop (basically left) is equal to the middle element (basically right), return the index of the outer loop count and middle plus 1
    4. Check to see if if the target minus the element at the count index is greater than the middle element, if so move the left pointer to the middle plus 1. Otherwise move the right pointer to the middle minus 1
- This solution is possible since the array that is given is already sorted 
- This algorithm has a time complexity of O(nlogn) since we are cutting the array in half with each step
