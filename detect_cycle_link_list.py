class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value  # The value of the node
        self.next = next    # Pointer to next node

def hasCycle(head):
    # make a set to store the nodes that have been visited
    visited_nodes = set()

    # make a pointer to traverse the linked list
    current = head

    # Iterate through linked list
    while current is not None:
        # If the current node has been visited before, a cycle is detected
        if current in visited_nodes:
            return 1  # Return 1 indicating that a cycle is present

        # or, add the current node to the visited nodes
        visited_nodes.add(current)

        # Move to the next node
        current = current.next

    # If the loop completes without detecting a cycle, no cycle
    return 0  # Return 0 for no cycle

# example usage:
# Creating a list with a cycle for demonstration purposes
node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2
node2.next = node1  # create cycle by pointing node2 back to node1

print(hasCycle(node1))  # Output will be 1, indicating a cycle occurs
