""" This file contains inplementations of the algorithms learned. Read this before interview along side your notes, to understand the implementation concretely."""


# Sorting Algorithms
# Bubble sort : Runs multiple passes and arranges adjacent elements in the order until no swaps left to end the pass. Easiest, but O(n2).
def bubble_sort(array):
    n = len(array)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1, swap if the element found is greater than the next element.
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


# Driver code to test bubble_sort
# a = [64, 34, 25, 12, 22, 11, 90]
# print(f'In put array is {a} and bubble sorted array is {bubble_sort(a)}')


# Merge Sort: Splits elements into single itemed arrays in halves (divide), merge operation from bottom to top (conquer) - compares elements in one list with another & arranges until big list again
def merge_sort(array):
    if len(array) > 1:
        # Finding the mid point of array
        mid = len(array) // 2  # integer division to make sure no float
        # Divide the array elements into left half & right half
        l = array[:mid]
        r = array[mid:]
        # Sorting the first half
        merge_sort(l)
        # Sorting the second half
        merge_sort(r)
        # The above code calls itself recursively until all elements are split into single item arrays
        # Initialize positions as first elements that we use later
        i = j = k = 0
        # Copy data to temporary arrays l[] and r[]
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                array[k] = l[i]  # k will be index in final sorted array. It is increasing slowly.
                i += 1  # if ith element is small, then add it..else add jth element
            else:
                array[k] = r[j]
                j += 1
            k += 1  # move onto a new position
        # Check if any element was left
        while i < len(l):
            array[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            array[k] = r[j]
            j += 1
            k += 1
    return array


# Driver code to test merge_sort()
# a = [64, 34, 25, 12, 22, 11, 90]
# print(f'Input array is {a} and merge sorted array is {merge_sort(a)}')


# Insertion sort: Usually applied for nearly sorted items. If negligible # of items to be sorted, then O(n), else O(n2). Runs a loop inside a loop to swap adjacent elements.
# Compare element with its predecessors and insert in right position, if in right position, move on..
def insertion_sort(array):
    # Traverse through 1 to len(array)
    for i in range(1, len(array)):
        key = array[i]
        # Move elements of array[0,...i-1] that are greater than key, to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


# Driver code to test insertion_sort(array)
# a = [64, 34, 25, 12, 22, 11, 90]
# print(f'Input array is {a} and insertion_sorted array is {insertion_sort(a)}')

""" Search Algorithms """


# Binary search : It discards half of elements everytime. Takes O(log n) constant set of operations to split, adjusts elements if < / > current position until it reaches the item
def binary_search(array, key):
    if not array:
        return None
    n = len(array) // 2  # int division to avoid float
    if key == array[n]:
        return n
    if key > array[n]:  # if key is > nth position (mid), slice right part
        sliced = array[n + 1:]
    else:
        sliced = array[:n]
    return binary_search(sliced, key)  # Perform a binary search again until there's nothing to slice & if middle element is the key


# Driver code to check binary_search(array)
a = [64, 34, 25, 12, 22, 11, 90]
print(f'Input array is {a} and binary_search for array is {binary_search(array=a, key=90)}')


""" Searching in Graphs"""


# Depth First Search : It is similar to depth first traversal in tree, only a little different because here we don't want to visit the nodes again, hence backtrack from the node if it is the leaf.
# Depth first search involves searching the path for a node in a graph.
def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


# Using a Python dictionary to act as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
visited = set()  # Set to keep track of visited nodes
# Driver code to test DFS
# print(dfs(visited, graph, 'A'))


""" Hash table : """