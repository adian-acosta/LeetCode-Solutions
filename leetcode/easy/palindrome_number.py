class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x is a negative number it cannot be a palindrome
        if x < 0:
            return False
        
        reversed_x = 0
        # creating a copy of x to avoid accidental modifying to the original input
        copy = x

        # will reverse x and store the result in the reversed_x variable
        while copy > 0:
            reversed_x = (reversed_x * 10) + (copy % 10)
            copy //= 10
        
        # compare x to the reversed input, if equal then it is a palindrome otherwise return false
        return x == reversed_x