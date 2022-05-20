class Solution:
    def isPalindrome(self, x: int) -> bool: #return type is bool

        #base case
        if x < 0:
            return False

        else:
            y = str(x)

            if y[0] == y[len(y) - 1]:
                return True
