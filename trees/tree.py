import collections


class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Tree:
    parent = None
    path = []
    def createNode(self, data):
        return Node(data)


    def insert(self, root , data):
        node = root

    def insert(self, node, data):
        """
        Insert function will insert a node into tree.
        Duplicate keys are not allowed.
        """
        #if tree is empty , return a root node

        if node is None:
            return self.createNode(data)
        else:
            if data == node.data:
                return node
            elif data < node.data:
                node.left = self.insert(node.left, data)
            else:
                node.right = self.insert(node.right, data)
        return node

    def search(self, node, data):
        if node is None or node.data == data:
            return node
        if node.data < data:
            return self.search(node.right, data)
        else:
            return self.search(node.left, data)




    def deleteNode(root, data):

        if root is None:
            return root

        if data < root.data:
            root.left = Tree.deleteNode(root.left, data)

        elif (data > root.data):
            root.right = Tree.deleteNode(root.right, data)

        else:

            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = Tree.minValueNode(root.right)
            root.key = temp.data
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
            self.path.append(root.data)
            self.traverseInorder(root.right)
        return self.path

    def traversePreorder(self, root):
        if root is not None:
            self.path.append(root.data)
            self.traversePreorder(root.left)
            self.traversePreorder(root.right)
        return self.path

    def traversePostorder(self, root):
        if root is not None:
            self.traversePostorder(root.left)
            self.traversePostorder(root.right)
            self.path.append(root.data)
        return self.path

    def levelOrderTraversal(self, root):
        ans = []

        # Return Null if the tree is empty
        if root is None:
            return ans

        # Initialize queue
        queue = collections.deque()
        queue.append(root)

        # Iterate over the queue until it's empty
        while queue:
            # Check the length of queue
            currSize = len(queue)
            currList = []

            while currSize > 0:
                # Dequeue element
                currNode = queue.popleft()
                currList.append(currNode.val)
                currSize -= 1

                # Check for left child
                if currNode.left is not None:
                    queue.append(currNode.left)
                # Check for right child
                if currNode.right is not None:
                    queue.append(currNode.right)

            # Append the currList to answer after each iteration
            ans.append(currList)

        # Return answer list
        return ans

def main():
    root = None
    tree = Tree()
    root = tree.insert(root, 1)
    print(root)
    tree.insert(root, 11)
    tree.insert(root, 5)
    tree.insert(root, 6)
    tree.insert(root, 2)
    tree.insert(root, 7)
    #tree.insert(root, 80)

    print("Traverse Inorder")
    tree.traverseInorder(root)

    print("Traverse Preorder")
    tree.traversePreorder(root)

    print("Traverse Postorder")
    tree.traversePostorder(root)


if __name__ == "__main__":
    main()


