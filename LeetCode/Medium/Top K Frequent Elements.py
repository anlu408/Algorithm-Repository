'''
We utilize Bucket Sort here.

Use a hashmap to count frequency of each integer in nums.
Freq a special array where we pair the frequency of an element to each integer.

Lastly, results is created, which is another array. We start from the end
of the array and iterate to 0 with a step size of 1 and we repeat this k times.
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range (len(nums) + 1)]
        res = []

        for n in nums:
            count[n] = 1 + count.get(n,0)

        for n, c in count.items():
            freq[c].append(n)

        for i in range (len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
