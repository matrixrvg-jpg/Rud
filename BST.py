# Binary Search Tree (BST) - SPPU Practical

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# 1. Insert function
def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.data:
        root.left = insert(root.left, val)
    elif val > root.data:
        root.right = insert(root.right, val)
    return root

# 2. Inorder display function (sorted order)
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

# 3. Search function
def search(root, val):
    if root is None or root.data == val:
        return root
    if val < root.data:
        return search(root.left, val)
    return search(root.right, val)

# Helper for deletion: find smallest node in right subtree
def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# 4. Delete function
def delete(root, val):
    if root is None:
        return root
    
    if val < root.data:
        root.left = delete(root.left, val)
    elif val > root.data:
        root.right = delete(root.right, val)
    else:
        # Node with 0 or 1 child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        # Node with 2 children
        temp = min_value_node(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)
        
    return root

# --- Main Menu Program ---
root = None

while True:
    print("\n--- BST OPERATIONS ---")
    print("1. Insert")
    print("2. Display (Inorder)")
    print("3. Search")
    print("4. Delete")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        val = int(input("Enter value to insert: "))
        root = insert(root, val)
        print("-> Inserted successfully!")
        
    elif choice == 2:
        print("BST Elements (Inorder): ", end="")
        if root is None:
            print("[Tree is empty]")
        else:
            inorder(root)
            print()
            
    elif choice == 3:
        val = int(input("Enter value to search: "))
        if search(root, val):
            print("-> Value found in BST!")
        else:
            print("-> Value not found.")
            
    elif choice == 4:
        val = int(input("Enter value to delete: "))
        root = delete(root, val)
        print("-> Deletion operation completed.")
        
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Enter between 1 and 5.")