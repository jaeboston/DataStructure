#: implement logic for both encoding and decoding
#: Huffman Coding is a lossless data compression algorithem.

#: Two phases in encoding - building the Huffman tree (a binary tree), and generating the
#: encoded data.
#: A Huffman tree is built in a bottom-up approach
#: determine the frequency of each character in the message.

#: list to work as a priority queue, where a node that has lower
#: frequency should have a higher priority to be popped-out. THe following snapshot will
#: help you visualize the example considered above.


import sys
import logging
import heapq

logging.basicConfig(level=logging.INFO)


class TreeNode():

  def __init__(self, char, freq):
    self.char = char
    self.freq = freq
    self.left = None
    self.right = None
        

def dfs_traverse(node, path, output):

  #: base case
  if node.left == None and node.right == None: #: leaf node
    output[node.char] = ''.join(path.copy())
    return

  leftpath = path.copy()
  leftpath.append(0)
  dfs_traverse(node.left, path+['0'], output)
  dfs_traverse(node.right, path+['1'], output)


#:===============================================
def huffman_encoding_with_heap(data):

  #1: get the freq for each char
  freq_dict = {}

  for char in data:
    freq_dict[char] = freq_dict.get(char, 0)
    freq_dict[char] += 1
  
  #2: Create min heap and sort by freq
  min_heap = []

  for char, freq in freq_dict.items():
    heapq.heappush(min_heap, (freq, char))

  #3: build the Huffman tree
  while len(min_heap) >= 2:
    #: pop the two lowest freq (the freq. values are in tuple)
    one = heapq.heappop(min_heap)
    two = heapq.heappop(min_heap)
    node = TreeNode('', one[0]+two[0]) #: TreeNode(char, freq)
    
    #: check the type
    if type(one[1]) is str:
      node.left = TreeNode(one[1], one[0])
    else:
      node.left = one[1]
    if type(two[1]) is str:
      node.right = TreeNode(two[1], two[0])
    else:
      node.right = two[1]

    heapq.heappush(min_heap, (node.freq, node))


  #4: generate encoding data using DFS traverse 
  (freq, tree_root) = min_heap[0]
  encoder = {}
  dfs_traverse(tree_root, [], encoder)

  #5: Encode using the encoder
  output = []
  for char in data:
    output.append( encoder[char])


  return ''.join(output) , tree_root


#:===============================================
def huffman_decoding(data,tree):

  currentNode = tree
  
  output = []
  #: traverse the data and see if it hits the end node
  for char in data:
    if char == '0':
      currentNode = currentNode.left
    else:
      currentNode = currentNode.right

    if currentNode.char != '':
      output.append(currentNode.char)
      currentNode = tree

  return ''.join(output)




#:===============================================
#: TEST
#:===============================================
#: CASE 1
#code1, tree1 = huffman_encoding_with_heap('AAAAAAABBBCCCCCCCDDEEEEEE')
#print(code1)
#original1 = huffman_decoding(code1, tree1)
#print(original1)

#: CASE 2
code, treenode = huffman_encoding_with_heap('AAAAAAA')
print(code)
original = huffman_decoding(code, treenode)
print(original)

#: CASE 3
#code, treenode = huffman_encoding_with_heap('')
#print(code)
