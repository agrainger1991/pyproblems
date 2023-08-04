# Define the structure of a tree node
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value  # The value of the current node
        self.left = left    # Pointer to the left child
        self.right = right  # Pointer to the right child

# Function to insert a value into a binary search tree
def insert(root, value):
    # If the root is None, create and return a new node with the given value
    if root is None:
        return TreeNode(value)
    else:
        # If the value is greater than the current node's value,
        # insert it into the right subtree
        if root.value < value:
            root.right = insert(root.right, value)
        else:
            # If the value is less than or equal to the current node's value,
            # insert it into the left subtree
            root.left = insert(root.left, value)
    # Return the root of the (possibly updated) subtree
    return root

# Example usage
root = None
values_to_insert = [5, 3, 8, 2, 4, 7, 9]

# Loop through the values and insert them into the BST
for value in values_to_insert:
    root = insert(root, value)
    # After each insertion, root is updated to point to the root of the tree
