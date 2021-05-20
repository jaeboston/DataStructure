We want to build an Encoder/Decoder of alphabet characters using Huffman Tree.
Huffman Tree is a binary tree data structure. The leaf nodes of the tree consist of Tuple (Character, Frequency). The lowest frequency char will be on the most left node. A parent node's value will be the sum of two children nodes' frequency values.

The path from a root to a leaf node indicates the Huffman encoding. For example, a path from a root to a leaf node (D,2) has [0,0,0]. Because 0 shows a left node and 1 for a right node. Thus, the path [ 0,0,0] means that it traversed a left child node three times to get to the leaf node D. The path is the encoded output for the character, D.

The Encoder will use a Dictionary with a key as each unique alphabet character and a value as the Huffman tree path for the key. (i.e  {'D': '000'} )

The encoding process can be done in the following three steps.
Step 1: Building a Huffman Tree.
To build a Huffman Tree, I used a min. Heap data structure. Using the min. Heap, I made a Huffman Tree with the smallest frequency values on the leftmost node.
It takes O(N*logN) time complexity to build the tree using the min Heap, where N is the number of unique characters in the given input data.


Step 2: Building an Encoder
Once we have the Huffman tree, we will traverse the tree to build the Encoder. I used Depth-First-Search with the backtracking method to travel to every leaf node and record the path. It takes O(N*logN) time complexity to build the Encoder.
Because there are N characters to encode and each character takes LogN (the height of tree)

Step 3: Generating encoded string using the Encoder
The last step is to generate the encoded string using the Encoder. I go through each character's input data and use the character as a key in the Encoder to find associating value. It takes O(N) time complexity.

The time complexity of the entire encoding is O(N) for Huffman Tree, + O(N*logN) for Encoder + O(N) for the generation of the encoded string. Therefore, O(N*logN)

Decoding is a more straightforward process than encoding. The decoding function takes two parameters, the Huffman Tree we built in the Encoding process and the encoded strings.
We parse every character in the encoded string and use the character to traverse the Huffman Tree. Zero indicates traveling down to the left node, and one shows traveling down to the right node.
If we visit a leaf node which is a Tuple, then we capture the alphabet char then start from the root node again.
This process will take O(N) time complexity, where N is each character in the encoded string.

Therefore in terms of the time complexity.
The decoding process will take O(N).

The space complexity would be O(N) where N is the number of unique characters.
