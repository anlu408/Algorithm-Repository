'''
Brute force:
Go through each element in the array and check if the sum of any two values are equal to the target.
However, after iterating through the array starting from a certain element it is no longer included in future
iterations as its sum has already been checked with other elements in the array.

Optimized Solution:
Use a hashmap.
Each value in the array is added to the hashmap.
Note that the value is mapped to the index so that we can return the two values that have a sum equal to the target.

However, we subtract the target from the current element and check if that
value is currently in the hashmap. If it is, we know that the two sum condition is met
and all that's left is to return true.hashmap

Time & Space Complexity:
Time:
O(n) - Hashmap is created with each element in the array iterated through.
Space:
O(n) - Each element in array added to hashmap.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: #-> indicates the return type is a list
        hashmap = {} #creates a dictionary

        for i, n in enumerate(nums): #i and n are two different indexs that are both incremented at the end of the loop iteration
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i
        return
'''
Enumerate returns an index followed by the item.

Test case 1: [2,1,5,3] with target = 4

1st iteration:
i = 0, n = 2
diff = 4-2 = 2
diff is not in prev_map as prev_map is empty
prev_map[2] = 0

2nd iteration:
i=1, n = 1
hashmap = {2:0}
diff = 4-1 = 3
3 is not in prev_map
prev_map[3] = 1

3rd iteration:
i=2 n=5
hashmap = {2,0 , 3:1}
diff = 4-5 = -1
-1 is not in the hashmap
prev_map[-1] = 2

4th iteration:
i=3 n=3
hashmap = {2:0 , 3:1, -1:2}
diff = 4-3 = 1
1 is in the hashmap
prev_map[1], i is returned which is [1,3]

Test case 2: [2,7,11,15] with target = 9
1st iteration:
i = 0, n = 2
diff = 9-2 = 7
7 is not in hashmap.
hashmap[2] = 0

2nd iteration:
i = 1, n = 7
prev_map{2:0}
diff = 9-7 = 2
2 is in the hashmap
hashmap[2], i is returned. -> (0,1)
'''
