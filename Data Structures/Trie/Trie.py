'''
Tree based DS organizing info in hierarchy.
-Often used to store/search strings in a space/time efficient way
-Any node in trie can store non-repetitive characters.
-Every node stores link of next character of the strings
-Every node keeps track of end of string

Examples of usecases:
-Spell Checkers
-Auto completion for text

Common Trie Operations
-Creation
-Insertion
-Search
-Deletion

Insertion Method

Search Method:
Case 1: String does not exist in Trie -> Return the string DNE
Case 2: String exists in Trie
    1. Check root node and continue to the next node.
    2. Check for end of string after last character.
Case 3: String is a prefix of another string but DNE in Trie.
    1. Check root node, continue to next node if match.
    2. Check for end of string on last character -> does not exist, return false.

Delete Method
Case 1: Some prefix of string is the same as the one we want to delete
    1. Check root node, continue if match
    2. Check for end of string on last character of word searched
    3. Delete characters until the point where the overlap occurs.
Case 2: The string is a prefix of another string
    1. You can set the end of string on more than one letter
    2. String is a prefix of another string
Case 3:
'''

class node:
    def __init__(self):
        self.children = {}
        self.end_of_string = False

class trie:
    def __init__(self):
        self.root = node()

    def insert_string (self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            current.children.update({ch:node})
        current = node
        current.end_of_string = True
        print("Successfully Inserted")

    def search(self, word):
        current_node = self.root
        #Case 1
        for i in word:
            node = current_node.children.get(i)
            if node == None:
                return false
            current_node = node
        #Case 2
        if current_node.end_of_string == True:
            return True
        #Case 3: String is a prefix. Check for EOS after last character
        else:
            return False

def delete_string(root,word,index):
    ch = word[index]
    current_node = root.children.get(ch)
    delete_check = False
    #Case 1: Some prefix of string is the same as the one we want to delete

    if len(current_node.children) > 1:
        delete_string(root, word, index + 1)
        return False

    if index = len(word) - 1:
        current_node.end_of_string = False
