'''
From previous anagram questions, sorting is always a possible solution.
However given that the arrays in this question are tuples we end up with a
rather large time complexity.

nlogn to get each string sorted * m which is the size of the original array.

My first guess to this question would be to use hashmaps as that is the most
common solution for these types of questions.

Hashmap Solution:
We know that each string goes from a-z so there is at most 26 unique characters.

For each string we should count the number of each letter.
The key ends up being the number of each letter and the value being the list of
anagrams that hold the same value as the key.

Time & Space Complexity:
O(m*n)
where m is the number of elements in the strs array and n is the total number
of characters in the strings.


'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Maps count of each character to list of anagrams.
        hashmap = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26 #counter for each character

            for c in s:
                '''
                ord returns the ASCII value of the character
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
            #Groups together strings of the same key.
            hashmap[tuple(count)].append(s)

        return hashmap.values()
