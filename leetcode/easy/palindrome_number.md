### Palindrome Number (Time taken: 16 m 1 s)
- A easy solution would be to convert the input int into a string and use a two-pointer approach to check the front and back. But I chose to keep the input as an int for the added challenge.
- The approach:
  1. Check if the input is a negative number. If it is, return false early because negative numbers cannot be palindromes.
  2. Create a copy of the original input to avoid altering it accidentally.
  3. Reverse the number using an [arithmetic method](https://www.programiz.com/python-programming/examples/reverse-a-number).
  4. Compare the reversed number with the original. If they are the same, the number is a palindrome; otherwise, return false.