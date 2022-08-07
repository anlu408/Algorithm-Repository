'''
Anagram- A word formed by using the same letters as another word.

Hashmap soln:
Base case: Check if the two strings have the same length. If they don't, return False.
If they do, continue to iterate.

With a hashmap we count the occurrences of each letter. If the values of each match, return true. If they don't,
return false.

Time & Space Complexity:
Both Space & Time:
O(S+T) - Based on number of elements in S&T array.

Alternate Soln:
Sort S & T. If the sorted S and sorted T are not equal, return false.
'''
#Hashmap Soln
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #Base-case of Hashmap soln
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range (len(s)):
            '''
            Increments the count of whichever letter (the key) by 1.
            We must use 'get' in the case that the letter doesn't currently exist in the hashmap.

            The 2nd parameter in 'get' is just a default value. 0 is a default value so if the
            key doesn't currently exist, it will return 0.
            '''
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        #Iterating through hashmaps to confirm same count for each character (key).
        for x in countS:
            '''
            We use the get function again here to make sure that if
            there is a letter in S that does not exist in T that we
            just return false. If we did not use get here, the program
            would return an error.
            '''
            if countS[x] != countT.get(x, 0):
                return False

        return True
