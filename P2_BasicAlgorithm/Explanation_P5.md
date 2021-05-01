# Objective: 
we need to add the ability to list suffixes to implement our autocomplete feature. To do that, we need to implement a new function on the TrieNode object that will return all complete word suffixes that exist below it in the trie. For example, if our Trie contains the words ["fun", "function", "factory"] and we ask for suffixes from the f node, we would expect to receive ["un", "unction", "actory"] back from node.suffixes().


# Constraint: 
- Use recusion to collect suffixes

# Algorithm 

The suffixes() function in TriNode would use a helper function which is called recurssively as it traverses down the Trie. We can pass a list variable into this helper function to collect suffixes.


The helper function will add suffixes to the list variable if it finds the is_word property is set to True. The function recurssively traverse all the nodes in the Trie until the children property of its TrieNode is empty. We need to use the backtracking technique to collect proper suffixes.

At the end, we rereturn the list that contains all the suffixes.

The time complexity by functions: 
* the find() function in the Trie class would be O(m).The looup in dictionary would be O(1) but to check the existance of key would be O(m) where m is the number of nodes in the root children

* the insert() function in the Trie class would be O(n) where n is the number of characters

* the suffix() funciton in the TrieNode class woulbe be O(n*m) where n is the number of nodes it nees to visit and m is the number of children nodes in each of the n nodes.


The space complexity of the Trie would be O(n*m) n is the number of nodes and m is number of items in its nodes' children dictionary.

