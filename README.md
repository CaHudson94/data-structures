[![Build Status](https://travis-ci.org/cahudson94/data-structures.svg?branch=master)](https://travis-ci.org/CaHudson94/data-structures) [![Coverage Status](https://coveralls.io/repos/github/cahudson94/data-structures/badge.svg?branch=master)](https://coveralls.io/github/CaHudson94/data-structures?branch=master)

# Data Structures
Authors: Chris Hudson, Carlos Cadena, Morgan Nomura


All modules and tests located in src directory.

## Linked List
- module: linked_list.py
- test: test_linked_list.py
- public methods:

    ### push:
        - add a new node to the Linked List
    ### pop:
        - remove the head node of the Linked List,
        - and return it's value
    ### size:
        - returns the size of the Linked List
    ### search:
        - returns the node object for a given value,
        - or returns none if it is not in the Linked List
    ### remove:
        - remove a specific node from the Linked List
    ### display:
        - returns a the tuple of the List as a string

## Stack
- module: stack.py
- test: test_stack.py
- public methods:
    ### push:
        - add a new node to the top of the Stack
    ### pop:
        - remove the top node of the Stack,
        - and return it's value

## Doubly Linked List
- module: doubly_linked_list.py
- test: test_doubly_linked_list.py
- public methods:
    ### push:
        - add a new node to the front of the DLL
    ### append:
        - add a new node to the back of the DLL
    ### pop:
        - remove the head node of the DLL,
        - and return it's value
    ### shift:
        - remove the tail node of the DLL,
        - and return it's value
    ### remove:
        - remove a specific node from the DLL

## Queue
- module: que_.py
- test: test_que_.py
- public methods:
    ### enqueue:
        - add a new node to the back of the Queue
    ### dequeue:
        - remove the head node of the Queue,
        - and return it's value
    ### peek:
        - return the head of the Queue
    ### size:
        - returns the size of the Queue

## Dequeue
- module: deque.py
- test: test_deque.py
- public methods:
    ### append:
        - add a new node to the tail of the DQ
    ### appendleft:
        - add a new node to the head of the DQ
    ### pop:
        - remove the tail node of the DQ,
        - and return it's value
    ### popleft:
        - remove the head node of the DQ,
        - and return it's value
    ### peek:
        - return the tail of the DQ
    ### peekleft:
        - return the head of the DQ
    ### size:
        - returns the size of the DQ

## Binary Heap
- module: binheap.py
- test: test_binheap.py
- public methods:
    ### push:
        - add a new node to the Binary Heap
        - goes to the appropriate point
    ### pop:
        - remove and return the head of the Binary Heap,
        - and resets the heap accordingly

## Priority Queue
- module: priorityque.py
- test: test_priorityque.py
- public methods:
    ### insert:
        - add a new node to the PQ,
        - goes to the appropriate point
    ### pop:
        - remove the value with the highest priority,
        - and returns the value
    ### peek:
        - returns the value with the highest priority

## Graph One
- module: graph_1.py
- test: test_graph_1.py
- public methods:
    ### nodes:
        - returns a list of the nodes in the graph
    ### edges:
        - returns a list of the edges between nodes
    ### add_node:
        - add a new node to the graph
    ### has_node:
        - if the value give is on a node in the graph:
        - return True otherwise return False
    ### add_edge:
        - add a connection between two nodes
        - if the nodes are not in the graph adds them
    ### del_node:
        - removes the node from the graph
        - and any edges it is part of
    ### del_edge:
        - removes a connection between nodes
    ### neighbors:
        - returns a list of the nodes the value has
        - connections to
    ### adjacent:
        - returns True or False if:
        - the values are neighbors in some way or not
    ### depth_first_traversal:
        - returns a list of the path of the graph
        - traverses by depth level
    ### bredth_first_traversal:
        - returns a list of the path of the graph
        - traverses by breadth level

## Weighted Graph and Shortest Path
- module: graph_w.py
- test: test_graph_w.py
- public methods:
    ### nodes:
        - returns a list of the nodes in the graph
    ### edges:
        - returns a list of the edges between nodes
        - third parameter is the weight of connection
    ### add_node:
        - add a new node to the graph
    ### has_node:
        - if the value give is on a node in the graph:
        - return True otherwise return False
    ### add_edge:
        - add a connection between two nodes
        - if the nodes are not in the graph adds them
        - edges now have weight
    ### del_node:
        - removes the node from the graph
        - and any edges it is part of
    ### del_edge:
        - removes a connection between nodes
    ### neighbors:
        - returns a list of the nodes the value has
        - connections to
    ### adjacent:
        - returns True or False if:
        - the values are neighbors in some way or not
    ### depth_first_traversal:
        - returns a list of the path of the graph
        - traverses by depth level
    ### bredth_first_traversal:
        - returns a list of the path of the graph
        - traverses by breadth level
    ### b_f_shortest_path:
        - find the shortest path from start to end
        - uses bellman ford algorithm
    ### d_shortest_path:
        - find the shortest path from start to end
        - uses dijkstras algorithm

## Binary Search Tree
- module: bst.py
- test: test_bst.py
- contribs:
    - Erik Enderlein
    - http://pythoncentral.io/time-a-python-function/
- public methods:
    ### insert:
        - add a new node to the BST
        - incriments tracked variables
    ### delete:
        - delete a node from the BST
        - decriments tracked variables
    ### search:
        - return the node for the value
        - if not in the BST returns None
    ### size:
        - returns the size of the BST
    ### depth:
        - returns the amount of levels to the BST
    ### contains:
        - returns True if the value is in the BST
        - otherwise returns False
    ### balance:
        - returns the balance
        - difference between left and right depth
    ### pre_order:
        - returns the pre order traversal of the tree
        - returns as generator
    ### in_order:
        - returns the in order traversal of the tree
        - returns as generator
    ### post_order:
        - returns the post order traversal of the tree
        - returns as generator
    ### breadth_first:
        - returns the breadth first traversal of the tree
        - returns as generator


## Hash Table
- module: hash_table.py
- test: test_hash.py
- public methods:
    ### get:
        - find a value on a key in the hash table.
    ### set:
        - add a new key value pair to the hash table.
- hashes:
    ### naive:
        - We used a simple addative hash for our naive.
    ### advanced:
        - We made a hash using a few math operations using prime numbers on each of the string vlaues and added a diferentiator through the last value.

## Trie Tree
- module: trie.py
- test: test_trie.py
- public methods:
    ### insert:
        - O(n^2)
        - add a string to the tree
        - raise an error if it is in the tree
        - raise an error if the input is not a string
    ### contains:
        - O(1)
        - return true if the string is in the tree
        - else return false
        - raise an error if the input is not a string
    ### size:
        - O(1)
        - return the amount of strings in the tree
    ### remove:
        - O(n)
        - remove a string from the tree
        - raise an error if it is in the tree
        - raise an error if the input is not a string
    ### depth_traversal:
        - O(n^2)
        - return as a generator every word that has the given prefix


## Bubble Sort
- module: bubble_sort.py
- test: test_bubble_sort.py
- public methods:
    ### bubble_sort:
        - sort the input list.
        - if more then one type of input is given return error message.


## Insert Sort
- module: insert_sort.py
- test: test_insert_sort.py
- public methods:
    ### insert_sort:
        - sort the input list.
        - if more then one type of input is given return error message.


## Merge Sort
- module: merge_sort.py
- test: test_merge_sort.py
- public methods:
    ### mergesort:
        - sort the input list.
        - if more then one type of input is given return error message.


## Quick Sort
- module: quick_sort.py
- test: test_quick_sort.py
- public methods:
    ### quicksort:
        - sort the input list.
        - if more then one type of input is given return error message.


## Radix Sort
- module: radix_sort.py
- test: test_radix.py
- public methods:
    ### radixsort:
        - sort the input list.
        - if more then one type of input is given return error message.
