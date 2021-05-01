# Objective: 

we are going to implement an HTTPRouter like you would find in a typical web server.

The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return. In a dynamic web server, the content will often come from a block of code called a handler.

# Constraint: 
- Use the Trie data structure.

# Algorithm 

This algorithm will consist of three classes.
Route, RouteTrie and RouteTrieNode.

The RouteTrieNode is the foundation class implementing a Trie node.
The RouteTrieNode constructor will take a handler object as an input parameter.
It has two properties, handler and children, and one method, insert.
The handler property can hold the handler object passed in as the input parameter.
The children's property is a Dictionary object that holds other RouteTrieNode things.
The insert method takes a key and a handler. It can create a new RouteTrieNode object with the handler for the key and add it to the children's property.
The keys in the RouteTrieNode object are the route elements. For example, for /home/about, 'home' and 'about' are the route elements.

The RouteTrie is a class that forms a Trie. It uses the RouteTrieNode class to make a node. The RouteTrie has one property, root, which is the first RouteTrieNode in the RouteTrie. It has two methods, insert and find. The insert method takes the following three input parameters. It calls the RouteTrieNode's insert method to populate the root node's children recursively.

1. route_list: a list of route elements
2. handler: the handler for the last route element in the route_list
3. notFoundHandler: a default handler for the rest of the route element in the route_list

The find method takes route_list as an input parameter. It finds the route elements in the route_list and returns the hander for the last route element in the route_list. If any of the route elements in route_list is not found, then None is returned.

Last we implement the actual Router class. It will initialize itself with a RouteTrie for holding routes and associated handlers. It should also support adding a handler by the path and looking up a handler by the path. All of these operations will be delegated to the RouteTrie (insert, and find). The Router class has a method called, split_path which takes a path and creates a list of route elements. When calling the RouteTrie's insert and find methods, the split_path method will be called first to make route_list input arguments for those two methods.

The time complexity by functions: 
* the find() function in the RouteTrie class would be O(n) where n is the number of routes.The looup in dictionary would be O(1) but to check the existance of key would be O(n) where m is the number of nodes in the root children

* the insert() function in the Trie class would be O(n) where n is the number of routes


The space complexity of the Trie would be O(n*m) n is the number of nodes and m is number of items in its nodes' children dictionary.


