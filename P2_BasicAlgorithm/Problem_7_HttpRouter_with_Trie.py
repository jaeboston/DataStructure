# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, 
        # this is the root path or home page node
        self.root = RouteTrieNode(handler)


    def insert(self, route_list, handler, notFoundHandler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path

        cur_node = self.root

        for route in route_list:
            if route not in cur_node.children:
                cur_node.insert(route, notFoundHandler)
            cur_node = cur_node.children[route]
            
        cur_node.handler = handler


    def find(self, route_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        cur_node = self.root

        for route in route_list:
            if route not in cur_node.children:
                return None
            cur_node = cur_node.children[route]
        
        return cur_node.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.children = {}

    def insert(self, element, handler):
        # Insert the node as before
        self.children[element] = RouteTrieNode(handler)


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, rootHandler, notFoundHandler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router = RouteTrie(rootHandler)
        self.notFoundHandler = notFoundHandler
        

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie

        route_list = self.split_path(path)
        self.router.insert(route_list, handler, self.notFoundHandler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        route_list = self.split_path(path)
        handler = self.router.find(route_list)
        if handler == None:
            return self.notFoundHandler
        else:
            return handler

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return list(filter(None, path.split('/')))


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one