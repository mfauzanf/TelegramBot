def avl_is_balanced(newick):
    if len(newick) == 0:
        return True
    closing_parenthesis = -1
    for i in range(len(newick) - 1, -1, -1):
        if newick[i] == ')':
            closing_parenthesis = i
            break
    if len(newick) == 0:
        return True
    if newick[0] != '(' and closing_parenthesis == -1 and newick.count(',') == 0:
        return True
    elif newick[0] == '(' and closing_parenthesis != -1:
        newick_children = newick[1:closing_parenthesis]
        comma_separator = avl_newick_split_index(newick_children)
        if comma_separator == -1:
            left_height = avl_height(newick_children)
            right_height = 0
            if abs(left_height - right_height <= 1 and avl_is_balanced(newick_children)):
                return True
            else:
                return False
        else:
            left_height = avl_height(newick_children[:comma_separator])
            right_height = avl_height(newick_children[comma_separator + 1:])
            if abs(left_height - right_height <= 1 and avl_is_balanced(
                newick_children[:comma_separator])
                   and avl_is_balanced(newick_children[comma_separator + 1:])):
                return True
            else:
                return False
    else:
        raise ValueError("Input is not a valid AVL newick format.")


def avl_height(newick):
    if len(newick) == 0:
        return 0
    closing_parenthesis = -1
    for i in range(len(newick) - 1, -1, -1):
        if newick[i] == ')':
            closing_parenthesis = i
            break
    if newick[0] != '(' and closing_parenthesis == -1 and newick.count(',') == 0:
        return True
    elif newick[0] == '(' and closing_parenthesis != -1:
        newick_children = newick[1:closing_parenthesis]
        comma_separator = avl_newick_split_index(newick_children)
        if comma_separator == -1:
            left_height = avl_height(newick_children)
            right_height = 0
        else:
            left_height = avl_height(newick_children[:comma_separator])
            right_height = avl_height(newick_children[comma_separator + 1:])
        return 1 + max(left_height, right_height)
    raise ValueError("Input is not a valid AVL newick format.")


def avl_newick_split_index(newick):
    comma_separator = -1
    parenthesis_counter = 0
    comma_counter = 0
    if len(newick) == 0:
        return 0
    for i in range(0, len(newick)):
        if newick[i] == ',' and parenthesis_counter == 0:
            comma_separator = i
            comma_counter += 1
        if newick[i] == '(':
            parenthesis_counter += 1
        if newick[i] == ')':
            parenthesis_counter -= 1
    if comma_counter > 1:
        raise ValueError("Input is not a valid AVL newick format."
                         " Please check your input commas.")
    if parenthesis_counter != 0:
        raise ValueError("Input is not a valid AVL newick format."
                         " Please check your input parentheses.")
    return comma_separator
