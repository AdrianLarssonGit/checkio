def check_word_contained(counter_of_rows, row, word, vertical_list):
    try:
        start_index_in_row = row.index(word) + 1
    except ValueError:
        #Word begins on pos 0 of row
        start_index_in_row = 1

    end_index_in_row = start_index_in_row + len(word) - 1
    list_of_coordinates = []
    if vertical_list:
        list_of_coordinates.append(start_index_in_row)
        list_of_coordinates.append(counter_of_rows)
        list_of_coordinates.append(end_index_in_row)
        list_of_coordinates.append(counter_of_rows)
    else:
        start_index_in_row = row.index(word) + 1
        list_of_coordinates.append(counter_of_rows)
        list_of_coordinates.append(start_index_in_row)
        list_of_coordinates.append(counter_of_rows)
        list_of_coordinates.append(end_index_in_row)

    print(list_of_coordinates)


def checkio(text, word):
    text = text.replace(" ","")

    text_as_rows = [text.split("\n")]

    #This only works for word on one row
    counter_of_rows = 0
    vertical_list = False
    for element in text_as_rows:
        for row in element:
            counter_of_rows = counter_of_rows + 1
            if row.__contains__(word):
                check_word_contained(counter_of_rows,row,word, vertical_list)


    #Because list of list
    for row in text_as_rows:
        unpacked_list = row

    biggest_list = 0
    counter_of_rows = 0
    for element in unpacked_list:
        if counter_of_rows == 0:
            biggest_list = len(element)
            counter_of_rows += 1
        else:
            if len(element) > biggest_list:
                biggest_list = len(element)

            counter_of_rows += 1

    #To get equal length on each row so when we flip them with zip the longer rows do not get cut off
    final_list = []
    for element in unpacked_list:
        if len(element) <  biggest_list:
            element += ' ' * (biggest_list - len(element))
        final_list.append(element)


    # Zip the lines to turn them 90 degrees
    zipped = zip(*final_list)

    v_list = []
    for line in zipped:
        v_list.append(''.join(line))

    counter_of_rows = 0
    for row in v_list:
        counter_of_rows += 1
        if row.lower().__contains__(word):
            vertical_list = True
            check_word_contained(counter_of_rows,row,word,vertical_list)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
#     checkio("""DREAMING of apples on a wall,
# And dreaming often, dear,
# I dreamed that, if I counted all,
# -How many would appear?""", "ten") == [2, 14, 2, 16]
    checkio("DREAMING of apples on a wall,\nAnd dreaming often, dear,\nI dreamed that, if I counted all,\n-How many would appear?","ten")

