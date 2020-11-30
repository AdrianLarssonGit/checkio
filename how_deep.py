def how_deep(structure):
    # your code here
    structure_as_string = ''.join(str(structure))

    list_of_openings = []
    list_of_close = []
    for char in structure_as_string:
        if char == "(" or char == "[":
            list_of_openings.append(char)
        if char == ")" or char == "]":
            list_of_close.append(char)

    print(list_of_openings)
    print(list_of_close)

    #return list_of_openings


if __name__ == '__main__':
    # print("Example:")
    # print(how_deep((1, 2, 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    print(how_deep([1,[2],[3]]))
