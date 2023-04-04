# smlp
Simulation Based Learning Platform
Home Window

The Home Window is from where the user can start other modules. A new separate window is opened for every module. These windows though independent still run via the same single QApplication thread.

 

![image](https://user-images.githubusercontent.com/26642556/229671456-fce643a5-1f52-4141-85d2-b87b36398537.png)








Stack Window

Below is shown the stack window with 4 elements pushed onto the stack. The operations available are Push, Pop, Top, IsEmpty, and Size. Information about the push operation is also shown in the information box.

 



![image](https://user-images.githubusercontent.com/26642556/229671507-0ef168af-62d7-421c-b026-b11fc800df31.png)







Queue Window

Queue is a FIFO data structure. The front of the queue is marked with a green label whereas the rear is marked with red label. The operations other than these are dequeue, emptiness and size.

 



![image](https://user-images.githubusercontent.com/26642556/229671531-780aae63-f0af-446f-980a-160bed2a56a6.png)










Linked List

The arrow head marks the next pointer (or reference) of the node. User has the option to delete or insert at beginning or at some location or at the last. Mode must be selected before inserting any node.
![image](https://user-images.githubusercontent.com/26642556/229671546-73e5a126-6811-46f0-aba4-9ede6ea35792.png)

 

Searching

User can input the array by separating individual elements using ‘,’ comma. Two searching algorithms are available:- Binary search and Linear search
 ![image](https://user-images.githubusercontent.com/26642556/229671561-c0af0372-668a-4654-9e22-4b1debe9a3c9.png)



Tree

There are two implementations of the tree. Binary Search Tree (BST) and AVL Tree.
Binary Search Tree is a binary tree where each subtree to left has smaller value elements than the root and each subtree to right has larger value than the root.

AVL tree is a height balancing tree where difference between the heights of any two subtrees cannot be more than logn. 

Traversals are also possible for the two trees and their output as well as a smooth animation is also shown. However the animation speed cannot be adjusted.
 

![image](https://user-images.githubusercontent.com/26642556/229671582-ac73886e-2010-4a50-9dc8-5fb1451d7bd3.png)









Graph Basic Operations

In all the graphs the user has to first draw the graph and then apply operations. Certain operations may result in garbage value if the graph is not suitable for the operation. 

The output is shown in a simple text and mostly corresponds to the unformatted array solution returned by most algorithms.

 
 
![image](https://user-images.githubusercontent.com/26642556/229671598-499ac722-dbb0-47e6-80fc-4fb6d8abad84.png)
![image](https://user-images.githubusercontent.com/26642556/229671611-761e2d1a-7a3e-46d5-bea5-6f99ebb71beb.png)
 
Shortest Paths

There are three shortest path algorithms implemented.
Single source Djikstra and Bellman Ford. All Pairs Floyd Warshall. Note that running Djikstra with negative edge weights will result in an error.



![image](https://user-images.githubusercontent.com/26642556/229671660-de6c4cf4-7769-42c5-a2ec-2ccf8892679f.png)









Miscellaneous Graph

The operations here are Depth First Search and Breadth First Search. The Hamiltonian Cycle is disabled because it necessarily requires for the graph to be a tournament cycle.

 


![image](https://user-images.githubusercontent.com/26642556/229671690-94f198ad-db67-4367-b71c-9890ca618e1e.png)








Sorting Algorithm

The user can input the array and click on generate which will draw bars on the screen, height adjusted and normalized. The user has the option to select from various sorting algorithms and also select the animation speed using the slider.

 ![image](https://user-images.githubusercontent.com/26642556/229671674-36faea1d-67e7-4456-b3ef-50e515656987.png)




