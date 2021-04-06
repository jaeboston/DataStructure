# Objective: 
we need to add the ability to list suffixes to implement our autocomplete feature. To do that, we need to implement a new function on the TrieNode object that will return all complete word suffixes that exist below it in the trie. For example, if our Trie contains the words ["fun", "function", "factory"] and we ask for suffixes from the f node, we would expect to receive ["un", "unction", "actory"] back from node.suffixes().


# Constraint: 
- Use recusion to collect suffixes

# Algorithm 

The suffixes() function in TriNode need a helper function which is called recurssively as we traverse down the Trie. We can pass a list variable into this helper function to collect suffixes.

The helper function has a base case when the children property of its TrieNode is empty. It returns the list variable.

In every recursion, it checks is_word property and if the property is set to True then we append the suffixes to the list variable.


