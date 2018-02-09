
def height(tree):
    h = 0
    s = []
    for i in range(0, len(tree)):
        if tree[i] == '(':
            s.append('(')
            if len(s) > h:
                h += 1
        elif tree[i] == ')':
            if(len(s) == 0):
                raise ValueError("Invalid input, input must be a valid newick format")
            s.pop()
    if(len(s) > 0):
        raise ValueError("Invalid input, input must be a valid newick format")
    return h
