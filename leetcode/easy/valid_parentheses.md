### Valid Parentheses (Time taken: 9 m 13 s)
- Used a stack to keep track of each opening bracket encountered and used it to pair with any closing brackets that were found within the string
- The approach:
  1. Check if the current pointer is a opening bracket if so push it on to the stack and continue along the string
  2. See if the stack is empty, if the loop continues and the current pointer is not a opening bracket then its a closing bracket. If the stack empty then return false as there is no pair
  3. If the stack is not empty and the current pointer is not a opening bracket then match the element with the top of the stack and pop it, if they match then continue otherwise return false
  4. After looping through the string check if the stack is empty, if empty then each bracket was paried and can return true. Otherwise return false