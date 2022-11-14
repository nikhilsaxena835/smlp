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


    def delete_Node(self, root, key):
        parent = None
        curr = root
        while curr and curr.data != key:

            # update the parent to the current node
            parent = curr

            # if the given key is less than the current node, go to the left subtree;
            # otherwise, go to the right subtree
            if key < curr.data:
                curr = curr.left
            else:
                curr = curr.right

        # return if the key is not found in the tree
        if curr is None:
            return root

        # Case 1: node to be deleted has no children, i.e., it is a leaf node
        if curr.left is None and curr.right is None:

            # if the node to be deleted is not a root node, then set its
            # parent left/right child to None
            if curr != root:
                if parent.left == curr:
                    parent.left = None
                else:
                    parent.right = None

            # if the tree has only a root node, set it to None
            else:
                root = None

        # Case 2: node to be deleted has two children
        elif curr.left and curr.right:

            # find its inorder successor node
            successor = self.minValueNode(curr)

            # store successor value
            val = successor.data

            # recursively delete the successor. Note that the successor
            # will have at most one child (right child)
            self.delete_Node(root, successor.data)

            # copy value of the successor to the current node
            curr.data = val

        # Case 3: node to be deleted has only one child
        else:

            # choose a child node
            if curr.left:
                child = curr.left
            else:
                child = curr.right

            # if the node to be deleted is not a root node, set its parent
            # to its child
            if curr != root:
                if curr == parent.left:
                    parent.left = child
                else:
                    parent.right = child

            # if the node to be deleted is a root node, then set the root to the child
            else:
                root = child
        return root

    def minValueNode(self, curr):
        while curr.left:
            curr = curr.left
        return curr

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



"""def main():
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
    tree.traversePostorder(root)"""


"""if __name__ == "__main__":
    main()
"""

