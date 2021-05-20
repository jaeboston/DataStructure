The `intersection` function will create a two `sets`. It iterates thru the first `set` and if the item in the first set is found in the second set, append the item into a new linked list object.

The time complexity of the `intersection` function would be O(N*M) where the N is the number of items in the first linked list and M is the number of items in the second linked list.

The `union` function will create a two `sets`. Then it uses the `union` function in the `set` class. Once we have a new `set` object with union of the two `sets`, it iterate thru each item in the new `set` and create a new `linked list`.

The time complexity of the function would be O(N) where N is the sum of items in the two sets.

The space complexity would be O(N) where N is the number of items in both of the linked lists.
