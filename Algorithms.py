'''1. Sorting Algorithms
Bubble Sort
What it Does: Repeatedly steps through the list, compares adjacent 
elements, and swaps them if they are in the wrong order.
Use: Simple, but inefficient for large datasets.
Code: python'''
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
'''Quick Sort
What it Does: Divides the array into sub-arrays based on a pivot element
and recursiverly sorts the sub-arrays.
Use: Efficient for large datasets.
Code: python '''
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
'''2. Search Algorithms
Binary Search
What it Does: Efficiently finds the position of a target value within a sorted array.
Use: Only works on sorted data.
Code:python'''
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
'''3. Graph Algorithms
Depth-First Search (DFS)
What it Does: Explores as far down a branch as possible before backtracking.
Use: Used in applications like topological sorting, detecting cycles.
Code: python'''
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next_node in graph[start] - visited:
        dfs(graph, next_node, visited)
    return visited

'''Breadth-First Search (BFS)
What it Does: Explores all neighbors at the present depth before moving on to
nodes at the next depth level.
Use: Shortest path in unweighted graphs, level-order traversal of trees.
Code:python '''
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited
'''4. Dynamic Programming Algorithms
Fibonacci Sequence
What it Does: Calculates the nth number in the Fibonacci sequence.
Use: Shows the basic idea of dynamic programming, storing results of subproblems
to avoid recomputation.
Code:python'''
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

'''Knapsack Problem
What it Does: Finds the most valuable subset of items that fit into a knapsack of
fixed capacity.
Use: Optimization problems in resource allocation.
Code:python '''
def knapsack(weights, values, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]
'''5. Greedy Algorithms
Dijkstra’s Algorithm
What it Does: Finds the shortest path between nodes in a graph.
Use: Network routing, shortest path in weighted graphs.
Code: python'''
import heapq

def dijkstra(graph, start):
    pq = []
    heapq.heappush(pq, (0, start))
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances
'''6. Backtracking Algorithms
N-Queens Problem
What it Does: Places N queens on an N×N chessboard so that no two queens
threaten each other.
Use: Solving constraint satisfaction problems.
Code:python'''
def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        return True

    def solve(board, col):
        if col >= n:
            return True
        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1
                if solve(board, col + 1):
                    return True
                board[i][col] = 0
        return False

    board = [[0] * n for _ in range(n)]
    if solve(board, 0):
        return board
    else:
        return None
'''7. Divide and Conquer Algorithms
Merge Sort
What it Does: Divides the array into halves, sorts each half, and merges
them back together.
Use: Efficient sorting algorithm with guaranteed performance.
Code:python'''
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
'''8. String Algorithms
KMP Algorithm (Knuth-Morris-Pratt)
What it Does: Searches for occurrences of a word within a main text string.
Use: String matching in text processing. Code:python'''
def kmp_search(pattern, text):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length-1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = compute_lps(pattern)
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return





