def frequency_sorting(numbers):
    numbers.sort()

    i = 0
    temp_list = []
    final_list = []
    while i < len(numbers):
        try:
            if numbers[i] != numbers[i + 1]:
                temp_list.append(numbers[i])
                final_list.append(temp_list)
                temp_list = []
            else:
                temp_list.append(numbers[i])
        except IndexError:
            temp_list.append(numbers[i])
            final_list.append(temp_list)
        i += 1

    for element in final_list:
        if type(element) == int:
            list_from_single_element = [element]
            final_list.append(list_from_single_element)
            final_list.remove(element)

    final_list.sort(key=len, reverse=True)

    list_to_send = []

    for element in final_list:
        for number in element:
            list_to_send.append(number)

    return list_to_send


if __name__ == '__main__':
    # print("Example:")
    # print(frequency_sorting([1, 2, 3, 4, 5]))
    #
    # #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert frequency_sorting([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Already sorted"
    # assert frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3]) == [4, 4, 4, 3, 3, 11, 11, 7, 13], "Not sorted"
    print(frequency_sorting([5, 6, 13, 99, 45, 34, 99, 6, 6, 45]))
