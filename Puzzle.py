import heapq


def solve_puzzle(Board, Source, Destination):
    """
    Finds and returns the path that covers the minimum number of cells of a
    puzzle traveling from the source to the destination cell.
    :param Board: Puzzle board as a list of lists. Each list represents a row
            in the puzzle. Each element is either â€˜-â€™ for an empty cell
            (passable) or â€˜#â€™ for an obstacle (impassable)
    :param Source: Tuple representing the indices of the starting position
    :param Destination: Tuple representing the indices of the goal position
    :return: List of tuples representing the indices of each position in the
            solution path, plus a string representing the directions taken
    """
    # Handle edge case if Source is also the Destination cell
    if Source == Destination:
        return [Source]

    # Use dictionary (initialized with Source cell) to store puzzle cells as
    # the keys and the value as a list of [min path distance from source to
    # cell, list of indices in the min distance path, and string of directions]
    min_path_dict = {Source: [0, [Source], '']}

    # use priority queue to track the min distance path starting with Source
    pq = [(0, Source)]

    while len(pq) > 0:
        # pop cell from priority queue that keeps path with overall min distance
        min_path, cell = heapq.heappop(pq)

        # find all valid neighbors of popped cell using helper function
        neighbors = find_neighbors(Board, cell)

        # for each neighbor, update min_path_dict if necessary
        for neighbor, direction in neighbors:
            # min distance from source to current cell is popped min_path + 1
            path_dist = min_path + 1

            # update dict if neighbor not in dict or path_distance is smaller
            if neighbor not in min_path_dict or path_dist < min_path_dict[neighbor][0]:
                # create copy of path list of indices and append current cell
                path = min_path_dict[cell][1].copy()
                path.append(neighbor)

                # append the direction to the directions string
                directions = min_path_dict[cell][2] + direction
                min_path_dict[neighbor] = [path_dist, path, directions]

                # if Destination is reached, return relevant list slice of dict
                if neighbor == Destination:
                    return min_path_dict[neighbor][1:]

                # update the priority queue
                heapq.heappush(pq, (min_path_dict[neighbor][0], neighbor))

    # if Destination is not reached, return None
    return None


def find_neighbors(puzzle, cell):
    """
    Finds and returns all valid neighbors of a cell in given puzzle
    :param puzzle: Puzzle board as a list of lists
    :param cell: Cell that we want to find all valid neighbors
    :return: List that includes indices of neighbor and its direction
    """
    row = cell[0]
    col = cell[1]
    neighbors = []

    # left move possible if col index is greater than 0 and cell is not '#'
    if col > 0 and puzzle[row][col - 1] != '#':
        neighbors.append(((row, col - 1), 'L'))

    # up move possible if row index is greater than 0 and cell is not '#'
    if row > 0 and puzzle[row - 1][col] != '#':
        neighbors.append(((row - 1, col), 'U'))

    # right move possible if col index is less than puzzle width - 1
    if col < len(puzzle[0]) - 1 and puzzle[row][col + 1] != '#':
        neighbors.append(((row, col + 1), 'R'))

    # down move possible if row index is less than puzzle height - 1
    if row < len(puzzle) - 1 and puzzle[row + 1][col] != '#':
        neighbors.append(((row + 1, col), 'D'))

    return neighbors
