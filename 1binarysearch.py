'''All 25 Algorithms

SEARCHING
1) Linear Search.
2) Binary Search.✍️
3) Depth First✍️
4) Breadth First✍️

SORTING
1) Insertion Sort.
4) Merge Sort.✍️
5) Quick Sort.✍️
6) Counting Sort
2) Heap Sort
3) Selection Sort.

GRAPHS
1) Kruskal's Algo. ✍️
2) Dilkstra's Algo.
3) Bellman Ford Algo.
 4) Floyd Warshall Algo.
5) Topological Sort Algo.
6) Flood Fill Algo
7) Lee Algo

ARRAYS
1) Kadane's Algo.
2) Floyd's Cycle Detection Algo.
3) KMP Algo.
4) Quick Select Algo.
5) Boyer - More Majority Vote Algo.

BASICS
1) Huffman Coding Compression Algo.
 3) Union Find Algo.
2) Euclid's Algo.
'''


# iterative method


def binarysearch(num, target):
    (left, right) = (0, len(num) - 1)

    while left <= right:
        mid = (left + right) // 2

        if target == num[mid]:
            return mid

        elif target < num[mid]:
            right = mid - 1

        else:
            left = mid + 1

    return -1


if __name__ == '__main__':
    num = [2, 5, 6, 8, 9, 10]

    target = int(input("enter the number\n"))
    index = binarysearch(num, target)

    if index != -1:
        print('element found at index', index)
    else:
        print('element not in the list')
