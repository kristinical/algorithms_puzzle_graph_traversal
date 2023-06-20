# Applying graph traversal to solve a puzzle
#### Portfolio assignment for CS 325: Analysis of Algorithms course at Oregon State University

You are given a 2-D puzzle of size MxN, that has N rows and M column (M and N can be different). Each cell in the puzzle is either empty or has a barrier. An empty cell is marked by ‘-’ (hyphen) and the one with a barrier is marked by ‘#’. You are given two coordinates from the puzzle (a,b) and (x,y). You are currently located at (a,b) and want to reach (x,y). You can move only in the following directions:
- L: move to left cell from the current cell
- R: move to right cell from the current cell
- U: move to upper cell from the current cell
- D: move to the lower cell from the current cell

You can move to only an empty cell and cannot move to a cell with a barrier in it. Your goal is to reach the destination cells covering the minimum number of cells as you travel from the starting cell.

Example Board:

<img width="371" alt="Screen Shot 2023-06-20 at 1 50 15 PM" src="https://github.com/kristinical/algorithms_puzzle_graph_traversal/assets/63667873/ae5de160-878e-4cc9-aa86-a35ddc94d35a">

**Input**: puzzle, source, destination 
  
- **puzzle**: A list of lists, each list represents a row in the rectangular puzzle. Each element is either ‘-’ for empty (passable) or ‘#’ for obstacle (impassable). Example:

  <img width="263" alt="Screen Shot 2023-06-20 at 1 54 33 PM" src="https://github.com/kristinical/algorithms_puzzle_graph_traversal/assets/63667873/ee27a258-f038-4c8d-8f51-a87fd9c49861">

- **source**: A tuple representing the indices of the starting position, e.g. for the upper right corner, source=(0, 4).
- **destination**: A tuple representing the indices of the goal position, e.g. for the lower right corner, goal=(4, 4).

**Output**: A list of tuples representing the indices of each position in the path. The first tuple should be the starting position, or source, and the last tuple should be the destination. If there is no valid path, None should be returned. Not an empty list, but the None object.

### Describe an algorithm to solve the above problem
The approach I used for my solution incorporates BFS with a greedy technique by using a priority queue. I also use a dictionary to keep track of the visited cells (the dictionary keys) and 3 elements for each key/cell (stored as a list for each dictionary value): 1) minimum path distance from source to the current cell; 2) list of cell indices that are within the min distance path; and 3) string of directions.

### What is the time complexity of your solution?
For my implementation (written in Python3), I use the following data structures and methods, including their individual time complexities
(bolded time complexities below contribute to overall time complexity of my solution):
- min_path_dict: dictionary which adds/appends elements one a time as necessary. Each call in Python3 is O(1).
- **Outer while loop** that runs as long as the priority queue is not empty, which will run at most **O(n)** times where n is the number of cells that exist in the puzzle.
- pq: **priority queue** that uses Python’s heapq.heappop() and heapq.heappush() methods, which each run in **O(log(n))**.
- Helper find_neighbors() function runs in constant O(1) time and will return at most 4 neighbors.
- The number of neighbors is used to control an inner for loop which will run at most O(4) times, which is constant time.
- Therefore, **the total overall time complexity of my solution is: O(n log n).**
