'''
Brute force solution:
Set x to be the 0th value in the list.
Iterate through each element in the array until a duplicate is found.
If no duplicate is found after x is equal to the last value in the list,
return false.

Least Space Complexity:
Sort the array first and that way you only have to loop through
the array once.

More optimized guess soln:
-Use a hashtable and add each value from the list to the hashtable.
-If a value is already added to the hashtable, return true. That way
you don't have to iterate through the entire array unless you face the
worst-case scenario.
-If you have added every single value to the hashtable, return false.

Optimized soln:
Utilize Hashsets - Differs from hashmaps in that they do not allow for duplicates.
Add values from the array to the hashset and if you come across a duplicate,
return true. If not, return false.

***Note that the tradeoff for this solution is that you go from
O(1) time complexity to O(n) as a hashset is created where n is the
size of the array
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hashset = set()

        for i in nums:
            if i in hashset: #base-case: if i is in the hashset, return true.
                return True
            hashset.add(i) #Adds value to hashset
        return False
