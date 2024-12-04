
def __check_2D(array):
    if isinstance(array, list) and all(isinstance(row, list) for row in array):
        return True
    return False

def get_neighbors_positions(array, i, j) -> list:
    '''
    For a given position, check boundaries and return all valid positions of neighbors for a point in a 2D array.
    Neighbors are presented in clockwise order, beginning from the upper-left neighbor, looking like this:
    
    123\n
    8X4\n
    765
    
    Returns
    -------
    A list of positions in the format [[i1, j1], [i2, j2], ..., [in, jn]]
    [-1] if a 2D list is not passed.
    '''

    if not __check_2D(array):
        return [-1]
    
    valid_neighbors = []
    
    if i-1 >= 0 and j-1 >= 0:
        valid_neighbors.append([i-1, j-1])
    if i-1 >= 0:
        valid_neighbors.append([i-1, j])
    if i-1 >= 0 and j+1 < len(array):
        valid_neighbors.append([i-1, j+1])
    if j+1 < len(array):
        valid_neighbors.append([i, j+1])
    if i+1 < len(array) and j+1 < len(array):
        valid_neighbors.append([i+1, j+1])
    if i+1 < len(array):
        valid_neighbors.append([i+1, j])
    if i+1 < len(array) and j-1 >= 0:
        valid_neighbors.append([i+1, j-1])
    if j-1 >= 0:
        valid_neighbors.append([i, j-1])
    
    return valid_neighbors


def get_neighbors_values(array, i, j) -> list:
    '''
    For a given position, check boundaries and return all values of neighbors for a point in a 2D array.
    Neighbors are presented in clockwise order, beginning from the upper-left neighbor, looking like this:
    
    123\n
    8X4\n
    765
    
    Returns
    -------
    A list of values in the format [v1, v2, ..., vn]
    [-1] if a 2D list is not passed.
    '''
    
    neighbor_positions = get_neighbors_positions(array, i, j)
    if neighbor_positions == [-1]:
        return [-1]
    
    neighbor_values = []
    for position in neighbor_positions:
        neighbor_values.append(array[position[0]][position[1]])
    
    return neighbor_values
