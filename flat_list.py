# We are going to need recursion, and checking if we are at the bottom
# We can check that by looking at type, when type is == int we are at bottom.
# Constraint is that program can only be 140 char long

def flat_list(array):
    final_list = []

    def list_check(nested_list):
        for i in nested_list:
            if type(i) == list:
                list_check(i)
            else:
                final_list.append(i)
        return final_list

    list_check(array)
    return final_list

if __name__ == '__main__':
    # assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    # assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
     print(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]))
    # assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
