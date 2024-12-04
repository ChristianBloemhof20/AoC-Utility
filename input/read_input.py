
def get_input_by_line(fp) -> list:
    ''' Reads the input file and returns a list of each line.
        Example Return: ['abcde', 'fghij', ...] '''
    
    with open(fp) as f:
        input = []
        for line in f.readlines():
            input.append(line.strip())
    
    return input

def get_input_by_char(fp) -> list:
    ''' Reads the input file and returns a list of each line broken down by characters.
        Example Return: [['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ...] '''
    
    with open(fp) as f:
        input = []
        for line in f.readlines():
            input.append([char for char in line.strip()])
    
    return input
