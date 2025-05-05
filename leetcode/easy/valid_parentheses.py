class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            # if opening brackets then push it on to stack
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
                continue
            
            if len(stack) == 0:
                # there was a closing bracket in s but the stack is empty
                return False
            
            # match the bracket to the top of the stack
            if i == ")":
                if stack.pop() != "(":
                    return False
            elif i == "}":
                if stack.pop() != "{":
                    return False
            elif i == "]":
                if stack.pop() != "[":
                    return False

        # if the stack is empty then each bracket was paried
        return len(stack) == 0