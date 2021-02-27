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

logging.basicConfig(level=logging.INFO)

#:===============================================
#: implementation of minimum Heap using array
class MinHeap(object):

    #:------------------------------------------
    def __init__(self, init_size=10):
        self.cbt = [None for _ in range(init_size)]  #: initilize the array: use it as CBT (complete Binary Tree)
        self.next_index = 0

    #:------------------------------------------
    def size(self):
        return self.next_index

    #:------------------------------------------
    #: store data either a Tuple (freq, char) or TreeNode into the Heap
    def insert(self, data):

        self.cbt[self.next_index] = data
        
        #: heapify so than the next min value is at the top of the tree
        self._up_heapify()

        #: increase the index
        self.next_index += 1

        #: check
        #: Heap is full, increase the size
        if self.next_index >= len(self.cbt): 
            tmp = self.cbt
            self.cbt = [None for _ in range(2*len(self.cbt))]
            #: copy data
            for i in range(len(tmp)):
                self.cbt[i] = tmp[i]
    

    #:------------------------------------------
    def remove(self):
        """
        remove the (freq, char) Tuple from the Heap
    
        """
        #: make sure the heap is not empty
        if self.next_index == 0:
            return None

        #: reduce the next_item size
        self.next_index -= 1

        top_item = self.cbt[0]
        #: swap with the last item then heapify down, the next insert operation will overwrite the swapped value at next_index
        self.cbt[0],self.cbt[self.next_index] = self.cbt[self.next_index], self.cbt[0]

        self._down_heapify() #: to make sure the next min value is at the top of the tree

        return top_item #: return (freq, char) Tuple

    #:------------------------------------------
    def _up_heapify(self):
        """
        heapify so that the last element at next_index 
        parent item should be less than than the new item
        check all the way to the top
        """

        child_index = self.next_index #: before increment next_index
        
        while child_index >= 1: #: loop till parent can be the top of the tree
        
            #: get its parent index (use CBT property in array)
            parent_index = (child_index -1)//2

            #: check the element
            parent_element = self.cbt[parent_index] #: get a Tuple
            child_element = self.cbt[child_index] #: get a Tuple

            #: check the type of element (either Tuple or TreeNode)
            if type(parent_element) is TreeNode:
                parent_element_value = parent_element.value
            elif type(parent_element) is tuple:
                parent_element_value = parent_element[1] #: (char, freq) tutple

            #: check the type of element (either Tuple or TreeNode)
            if type(child_element) is TreeNode:
                child_element_value = child_element.value
            elif type(child_element) is tuple:
                child_element_value = child_element[1] #: (char, freq) tutple

            if parent_element_value > child_element_value:
                self.cbt[parent_index], self.cbt[child_index] = self.cbt[child_index], self.cbt[parent_index]
                child_index = parent_index 
            else:
                break
    
    #:------------------------------------------
    def _down_heapify(self):
        """
        after remove the top item
        the bottom item got placed at the top.
        go thru their children and make sure the parent is less than their childrend (min heap)
        """
        parent_index = 0

        while parent_index < self.next_index:

            left_child_index = parent_index*2+1
            right_child_index = parent_index*2+2

            #: get the parent element
            parent_element = self.cbt[parent_index]
            left_child_element = None
            right_child_element = None 

            #: get the children element
            if left_child_index < self.next_index:
                left_child_element = self.cbt[left_child_index]
            if right_child_index < self.next_index:
                right_child_element = self.cbt[right_child_index]

            #: check the type of element (either Tuple or TreeNode)
            if type(parent_element) is TreeNode:
                parent_element_value = parent_element.value
            elif type(parent_element) is tuple:
                parent_element_value = parent_element[1] #: (char, freq) tutple

            min_value = parent_element_value

            #: check with Left Element first
            if left_child_element is not None:
                
                #: check the type of element (either Tuple or TreeNode)
                if type(left_child_element) is TreeNode:
                    left_child_element_value = left_child_element.value
                elif type(left_child_element) is tuple:
                    left_child_element_value = left_child_element[1] #: (char, freq) tutple

                min_value = min(min_value, left_child_element_value)

            
            if right_child_element is not None:
                #: check the type of element (either Tuple or TreeNode)
                if type(right_child_element) is TreeNode:
                    right_child_element_value = right_child_element.value
                elif type(right_child_element) is tuple:
                    right_child_element_value = right_child_element[1] #: (char, freq) tutple

                min_value = min(min_value, right_child_element_value)

            #: now check which index has the min value
            if min_value == parent_element_value:
                #: all set just exit
                return
            elif min_value == left_child_element_value:
                #: swap
                self.cbt[parent_index], self.cbt[left_child_index] = self.cbt[left_child_index], self.cbt[parent_index]
                parent_index = left_child_index
            elif min_value == right_child_element_value:
                self.cbt[parent_index], self.cbt[right_child_index] = self.cbt[right_child_index], self.cbt[parent_index]
                parent_index = right_child_index

#:===============================================
class TreeNode(object):

    #:------------------------------------------
    def __init__(self, value=None):
        self.value = value
        self.leftNode = None
        self.rightNode = None
        

#:===============================================
def tree_print(node):

    #: leaf node
    if type(node) is tuple:
        logging.debug(f"node = {node}")
        return
    if node == None:
        return

    tree_print(node.leftNode)
    tree_print(node.rightNode)

    return


#:===============================================
def buildEncoder_backtracking(node, path, encoder):

    #: if leaf node
    if type(node) is tuple:
        logging.debug(f"node = {node}")
        encoder[node[0]] = ''.join(path.copy())
        return

    if node is None:
        return

    #: left node
    path.append('0')
    buildEncoder_backtracking(node.leftNode, path, encoder)
    
    #: backtracking by pop
    path.pop()
    
    #: right node
    path.append('1')
    buildEncoder_backtracking(node.rightNode, path, encoder)
    
    #: backtracking by pop
    path.pop()
    
    return

#:===============================================
def huffman_encoding_with_heap(data):
    """
    build the tree using min Heap
    """
    #: edge case when empty data
    if len(data) == 0:
        return None , None
    
    #: create a frequency map
    freq_map = {}
    for char in data:
        if char not in freq_map:
            freq_map[char] = 1
        else:
            freq_map[char] +=1

    #: create a min heap
    minHeap = MinHeap()

    #: insert the freq_map values into the heap to create a tree
    for item in freq_map.items():
        minHeap.insert(item)
    
    #: -- Generate Tree --

    #: only 1 item in the heap
    if minHeap.size() == 1:

        tmp1 = minHeap.remove()  
        new_node = TreeNode(tmp1[1]) #: extract the value
        new_node.leftNode = tmp1
        new_node.rightNode = None

        rootNode = new_node

    while minHeap.size() > 1:

        #: pop out the two items from the queue one for left node and the other for right node
        tmp1 = minHeap.remove() #: 
        tmp2 = minHeap.remove()  #: 

        #: create a new TreeNode
        new_node = TreeNode()
        new_node.leftNode = tmp1         #: set the left node
        new_node.rightNode = tmp2        #: set the right node

        #: extract the freq value from the left node : could be tuple for the leaf node or just TreeNode otherwise
        if type(tmp1) is TreeNode:
            left_node_value = tmp1.value
        elif type(tmp1) is tuple:
            left_node_value = tmp1[1] #: (char, freq) tutple

        #: extract the freq value from right node value : could be tuple for the leaf node or just TreeNode otherwise
        if type(tmp2) is TreeNode:
            right_node_value = tmp2.value
        elif type(tmp2) is tuple:
            right_node_value = tmp2[1]

        #: set the TreeNode value
        new_node.value = left_node_value + right_node_value #: set the parent node value

        #: check to see if the two childres has same frequency and both of them are tuple, left child should have alphabet order
        #: i.e (A,7) (C,7) then (A,7) should be left node and (C,7) should be right node
        if left_node_value == right_node_value and type(tmp1) is tuple and type(tmp2) is tuple:
            if tmp1[0]< tmp2[0]:
                new_node.leftNode = tmp1
                new_node.rightNode = tmp2
            else:
                new_node.leftNode = tmp2
                new_node.rightNode = tmp1

        #: check to see if the size queue is done
        if minHeap.size() == 0:
            rootNode = new_node
            break
        
        logging.debug(f'new node value = {new_node.value}')
        #: put new_node to the heap
        minHeap.insert(new_node)


    #: Build the encoder by traversing from root to leaf
    encoder = {}
    buildEncoder_backtracking(rootNode, [], encoder)

    logging.debug(f'encoder={encoder}')
    
    output = []
    for char in data:
        output.append(encoder[char])
    return ''.join(output), rootNode


#:===============================================
def huffman_encoding_with_queue(data):
    """
    build the tree using a queue
    then use backtracking 
    """

    #: edge case when empty data
    if len(data) == 0:
        return
    
    #: create a frequency map
    freq_map = {}
    for char in data:
        if char not in freq_map:
            freq_map[char] = 1
        else:
            freq_map[char] +=1

    #: create queue (FIFO) with lowest frquency first enter
    #: initially the queue will be filled with tuples which are going to be the leaf nodes
    sorted_char_by_freq = sorted(freq_map.items(), key=lambda x: x[1])

    rootNode = None

    #: Generate Tree

    #: only i item in the queue
    if len(sorted_char_by_freq) == 1:

        tmp1 = sorted_char_by_freq.pop(0) #: 
        new_node = TreeNode(tmp1[1]) #: extract the value
        new_node.leftNode = tmp1
        new_node.rightNode = None

        rootNode = new_node

    #: till 1 or less item left in the queue
    while len(sorted_char_by_freq) > 1:

        logging.debug(sorted_char_by_freq)

        #: pop out the two items from the queue one for left node and the other for right node
        tmp1 = sorted_char_by_freq.pop(0) #: 
        tmp2 = sorted_char_by_freq.pop(0) #: 

        #: create a new TreeNode
        new_node = TreeNode()
        new_node.leftNode = tmp1         #: set the left node
        new_node.rightNode = tmp2        #: set the right node

        #: extract the freq value from the left node : could be tuple for the leaf node or just TreeNode otherwise
        if type(tmp1) is TreeNode:
            left_node_value = tmp1.value
        elif type(tmp1) is tuple:
            left_node_value = tmp1[1] #: (char, freq) tutple

        #: extract the freq value from right node value : could be tuple for the leaf node or just TreeNode otherwise
        if type(tmp2) is TreeNode:
            right_node_value = tmp2.value
        elif type(tmp2) is tuple:
            right_node_value = tmp2[1]

        #: set the TreeNode value
        new_node.value = left_node_value + right_node_value #: set the parent node value

        #: check to see if the two childres has same frequency and both of them are tuple, left child should have alphabet order
        #: i.e (A,7) (C,7) then (A,7) should be left node and (C,7) should be right node
        if left_node_value == right_node_value and type(tmp1) is tuple and type(tmp2) is tuple:
            if tmp1[0]< tmp2[0]:
                new_node.leftNode = tmp1
                new_node.rightNode = tmp2
            else:
                new_node.leftNode = tmp2
                new_node.rightNode = tmp1


        #: check to see if the size queue is done
        if len(sorted_char_by_freq) == 0:
            rootNode = new_node
            break
        
        logging.debug(f'new node value = {new_node.value}')

        #: put ('', new_node.value) to the queue and sort it again : like priority queue
        for i in range(len(sorted_char_by_freq)):
            if type(sorted_char_by_freq[i]) is TreeNode:
                value2compare = sorted_char_by_freq[i].value

            elif type(sorted_char_by_freq[i]) is tuple:
                value2compare = sorted_char_by_freq[i][1]

            else: #: just numeric
                value2compare = sorted_char_by_freq[i]


            if new_node.value <= value2compare:
                sorted_char_by_freq.insert(i, new_node)
                break

            #: the last item
            if i == len(sorted_char_by_freq)-1:
                sorted_char_by_freq.insert(i+1, new_node)


    #: Build the encoder by traversing from root to leaf
    encoder = {}
    buildEncoder_backtracking(rootNode, [], encoder)

    logging.debug(f'encoder={encoder}')
    
    output = []
    for char in data:
        output.append(encoder[char])

    return ''.join(output), rootNode


#:===============================================
def huffman_decoding(data, tree):

    output = []
    node = tree
    for char in data:
        if char == '0':
            node = node.leftNode
        else:
            node = node.rightNode

        if type(node) is tuple:
            output.append(node[0])
            node = tree
        logging.debug(output)
    return ''.join(output)




#:===============================================
#: TEST
#:===============================================
#: CASE 1
code1, tree1 = huffman_encoding_with_heap('AAAAAAABBBCCCCCCCDDEEEEEE')
print(code1)
original1 = huffman_decoding(code1, tree1)
print(original1)

#code2, tree2 = huffman_encoding_with_queue('AAAAAAABBBCCCCCCCDDEEEEEE')
#print(code2)
#original2 = huffman_decoding(code2, tree2)
#print(original2)


#: CASE 2
code, treenode = huffman_encoding_with_heap('AAAAAAA')
print(code)
original = huffman_decoding(code, treenode)
print(original)

#: CASE 3
code, treenode = huffman_encoding_with_heap('')
print(code)
