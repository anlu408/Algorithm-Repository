class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: #-> indicates the return type is a list
        prev_map = {} #creates a dictionary

        for i, n in enumerate(nums): #i and n are two different indexs that are both incremented at the end of the loop iteration
            diff = target - n
            if diff in prev_map:
                return [prev_map[diff], i]
            prev_map[n] = i
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
i=1, n=1
prev_map = {2:0}
diff = 4-1 = 3
3 is not in prev_map
prev_map[3] = 1

3rd iteration:
i=2 n=5
prev_map = {2,0 , 3:1}
diff = 4-5 = -1
-1 is not in the hashmap
prev_map[-1] = 2

4th iteration:
i=3 n=3
prev_map = {2:0 , 3:1, -1:2}
diff = 4-3 = 1
1 is in the hashmap
prev_map[1], i is returned which is [1,3]

Test case 2: [2,7,11,15] with target = 9
1st iteration:
i = 0, n = 2
diff = 9-2 = 7
7 is not in hashmap.
prev_map[2] = 0

2nd iteration:
i = 1, n = 7
prev_map{2:0}
diff = 9-7 = 2
2 is in the hashmap
prev_map[2], i is returned. -> (0,1)
'''
