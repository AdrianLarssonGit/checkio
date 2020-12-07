def how_deep(structure):
    if isinstance(structure, list):
        return 1 + max(how_deep(item) for item in structure)
    else:
        return 0


if __name__ == '__main__':
    print(how_deep([1,2,3]))
