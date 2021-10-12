'''
Hash Function- A function that can be used to map arbitrarily sized data to fixed size.
Key- Input data by user
Hash Value- A value returned by Hash function
Hash Table- A data structure implementing an associative array abstract data type, a structure that
maps keys to values.
Collision- When two different keys to a hash function produce the same output.

Good hash functions
=distributes hash values uniformly across hash tables
-Uses all of the input data

Collision Resolution Techniques
Direct Chaining- implements buckets as Linked List and colliding elements are stored in this list.

Open Addressing- Colliding elements are stored in other vacant buckets. During storage and lookup they are found with probing.
- Linear probing: Places new key into closest empty following empty cell.
- Quadratic Probing- Adding arbitrary quadratic polynomial to the index until an empty cell is found
- Double Hashing- Intervals between porobes is computed by another hash function

Full Hash tables
Direct Chaining- This never occurs
Open Addressing- Create 2x Size of current hashtable and recall hashing for current keys you can then use one of the open addressing methods to place the key in the hashtable.

Pros and Cons of Resolution Techniques
Direct Chaining-
Pros:
- Hash table never gets full

Cons:
- Huged LL causes performance link

Open addressing
Pro:
- Easy Implementation

Cons:
When full, you must create a new hash table and that affects performance

Input size known -> Use open addressing.
With frequent deletion use Direct Chaining

Practical Uses of Hashing
Password verification
File systems- file path mapped to physical location on disk

Pros/Cons of hashing
+ On average, Insertion/Deletion/Search takes O(1) time complexity
- When hash function is not good enough it takes O(N) time complexity
'''
