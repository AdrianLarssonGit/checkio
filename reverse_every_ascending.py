def reverse_ascending(items):
    ##Check to see if next item is bigger, add to list.
    ##If next item is not bigger. Stop and create a new list.

    list_of_lists_to_be_reversed = []
    start_list = []
    counter = 0
    while counter < len(items):
        i = items[counter]
        if counter + 1 == len(items):
            next_i_temp = items[-1:]
            next_i = next_i_temp[0]
        else:
            next_i = items[counter + 1]

        if next_i == i:
            start_list.append(i)
            list_of_lists_to_be_reversed[-1:].append(i)
        elif next_i > i:
            start_list.append(i)
        elif next_i <= i:
            start_list.append(i)
            list_of_lists_to_be_reversed.append(start_list)
            start_list = []
        else:
            start_list.append(i)
            list_of_lists_to_be_reversed.append(start_list)

        counter += 1

    list_of_lists_to_be_reversed.append(start_list)
    for list in list_of_lists_to_be_reversed:
        list.reverse()

    final_list = []
    for list in list_of_lists_to_be_reversed:
        for item in list:
            final_list.append(item)

    return (final_list)


if __name__ == '__main__':
    print(reverse_ascending([1,2,1]))
