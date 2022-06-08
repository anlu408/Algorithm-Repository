class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26 #counter for each character

            for c in s:
                '''
                ASCII values are consecutive. So for example
                A = 97
                B = 98
                C = 99
                ...etc.

                To set A to be the first value counted it has to be at index
                0. Subtract the ascii value of A from each letter after A
                to count each letter correctly in the count array
                '''
                count[ord(c) - ord('a')] += 1

            hashmap[tuple(count)].append(s)

        return hashmap.values()
