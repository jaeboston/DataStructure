class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
child_user = "child_user"
child.add_user(child_user)
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


#Write a function that provides an efficient look up of whether the user is in a group.

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if len(group.users)>0:
        if user in group.users:
            return True

    if len(group.groups) > 0:
        for sub_group in group.groups:
            return is_user_in_group(user, sub_group)

    else:
        return False


#: Test functions
#     
print(is_user_in_group("sub_child_user", parent)) #: True
print(is_user_in_group("child_user", parent)) #: True

print(is_user_in_group("other_child_user", parent)) #: False
print(is_user_in_group("", parent)) #: edge case testing False
print(is_user_in_group("child", parent)) #: False