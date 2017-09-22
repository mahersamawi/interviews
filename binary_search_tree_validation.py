'''
Question: Given the root of a tree, check if it is a binary search tree (unbalanced vs balanced solutions)
Solution: 2 Ways
1) Inorder travseral of the tree and check if list return is sorted (does not work with duplicates) 
2) Pass in the min max (initially pass in a very large and very small number) of each level and check nodes based on the left is less than the root and right
    is greater than the root and the left is greater than that min and the right is less than that max
'''
import copy


class Tree(object):

    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data


def check_valid_bst_inorder(root):
    ret_list = []
    check_bst_inorder(root, ret_list)
    sorted_list = copy.deepcopy(ret_list)
    sorted_list.sort()
    return (ret_list == sorted_list)


def check_bst_inorder(root, counter_list):
    if root is None:
        return
    check_bst_inorder(root.left, counter_list)
    counter_list.append(root.data)
    check_bst_inorder(root.right, counter_list)


def check_valid_bst(root):
    return check_bst_helper_balanced(root, -9999999, 999999)


# Unbalanced
def check_bst_helper(root, min_val, max_val):
    if root is None:
        return True
    if root.data > max_val or root.data < min_val:
        return False

    return check_bst_helper(root.left, min_val, root.data) and check_bst_helper(root.right, root.data, max_val)


# Balanced
def check_bst_helper_balanced(root, min_val, max_val):
    if root is None:
        return True
    if (root.left.data > root.data or root.right.data < root.data):
        return False
    if (root.left.data > min_val or root.right < max_val):
        return check_bst_helper(root.left, min_val, root.data) and check_bst_helper(root.right, root.data, max_val)
    return False


def main():
    root = Tree(4)
    root.left = Tree(2)
    root.right = Tree(5)
    root.left.left = Tree(1)
    root.left.right = Tree(3)
    if (check_valid_bst(root)):
        print "Is BST"
    else:
        print "Not a BST"

    root2 = Tree(10)
    root2.left = Tree(6)
    root2.right = Tree(14)
    root2.left.left = Tree(3)
    root2.left.right = Tree(12)
    root2.right.left = Tree(11)
    root2.right.right = Tree(16)
    if (check_valid_bst_inorder(root2)):
        print "Is BST"
    else:
        print "Not a BST"

if __name__ == '__main__':
    main()
