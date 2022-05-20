def guessNumber(self, n: int) -> int:
        if n == 1: #base case
            return 1

        low = 0
        high = n

        while low <= high:
            mid = int((low+high)/2)
            pick = guess(mid)

            if pick == 0:
                return mid
            elif pick == 1:
                low = mid + 1
            else:
                high = mid - 1

'''
Utilizes Divide & Conquer to solve problem.
Step 1: We guess the middle value between 1 and n (n/2) and set pick equal to the guess
Step 2: We check pick for 0, 1 or -1. If 0 , return mid. If 1, increase low so that
we guess a number higher than n/2. If -1 we decrease our guess to below mid.
'''
