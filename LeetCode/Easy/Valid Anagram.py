'''
Anagram- A word formed by using the same letters as another word.

Hashmap soln:
Base case: Check if the two strings have the same length. If they don't, return False.
If they do, continue to iterate.

Continue by using a hashmap to count the number of each letter that appears in both
string s and string t. If the values of each match, return true. If they don't,
return false.

Alternate Soln:
Sort S & T. If the sorted S and sorted T are not equal, return false.
'''
#Hashmap Soln
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): #Base-case of Hashmap soln
            return False

        countS, countT = {}, {}

        for i in range (len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for x in countS:
            if countS[x] != countT.get(x, 0):
                return False

        return True
