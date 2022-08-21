class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Tree:
    parent = None

    def createNode(self, data):
        return Node(data)

    def insert(self, root , data):
        node = root
        if node is None:
            return self.createNode(data)

        # if data is smaller than parent , insert it into left side
        else:
            if data == node.data:
                return node
            elif data < node.data:
                print("go left")
                node.left = self.insert(node.left, data)
            else:
                print("go right")
                node.right = self.insert(node.right, data)
        return node

    def search(self, node, data):
        """
        Search function will search a node into tree.
        """
        # if root is None or root is the search data.
        if node is None or node.data == data:
            return node

        if node.data < data:
            return self.search(node.right, data)
        else:
            return self.search(node.left, data)




    def deleteNode(root, data):

        # Base Case
        if root is None:
            return root

        # If the key to be deleted
        # is smaller than the root's
        # key then it lies in  left subtree
        if data < root.data:
            root.left = Tree.deleteNode(root.left, data)

        # If the kye to be delete
        # is greater than the root's key
        # then it lies in right subtree
        elif (data > root.data):
            root.right = Tree.deleteNode(root.right, data)

        # If key is same as root's key, then this is the node
        # to be deleted
        else:

            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with two children:
            # Get the inorder successor
            # (smallest in the right subtree)
            temp = Tree.minValueNode(root.right)

            # Copy the inorder successor's
            # content to this node
            root.key = temp.data

            # Delete the inorder successor
            root.right = Tree.deleteNode(root.right, temp.data)

        return root

    def minValueNode(node):
        current = node
        # loop down to find the leftmost leaf
        while (current.left is not None):
            current = current.left

        return current

    def traverseInorder(self, root):
        if root is not None:
            self.traverseInorder(root.left)
            print(root.data)
            self.traverseInorder(root.right)

    def traversePreorder(self, root):
        if root is not None:
            print(root.data)
            self.traversePreorder(root.left)
            self.traversePreorder(root.right)

    def traversePostorder(self, root):
        if root is not None:
            self.traversePostorder(root.left)
            self.traversePostorder(root.right)
            print(root.data)

    def getParent(target, root):
        parent, node = None, root
        while True:
            if node is None:
                return None

            if node.data == target:
                return parent.data

            if target < node.data:
                parent, node = node, node.left
            else:
                parent, node = node, node.right



def main():
    root = None
    tree = Tree()
    root = tree.insert(root, 1)
    print(root)
    tree.insert(root, 11)
    print("Parent of 11: ",Tree.getParent(11, root))
    tree.insert(root, 5)
    print("Parent of 5: ",Tree.getParent(5, root))
    tree.insert(root, 6)
    print("Parent of 6: ",Tree.getParent(6, root))
    tree.insert(root, 2)
    print("Parent of 2: ",Tree.getParent(2, root))
    tree.insert(root, 7)
    print("Parent of 7: ",Tree.getParent(7, root))
    #tree.insert(root, 80)

    print("Traverse Inorder")
    tree.traverseInorder(root)

    print("Traverse Preorder")
    tree.traversePreorder(root)

    print("Traverse Postorder")
    tree.traversePostorder(root)


if __name__ == "__main__":
    main()


