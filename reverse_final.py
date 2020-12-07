#After some thinking I got to this instead 
def reverse_ascending(items):

    result_list = []

    temp = []
    temp.append(items[0])
    for i in range(1, len(items)):
        
        if items[i-1] < items[i]:
            temp.append(items[i])
        else:
            result_list.append(temp)
            temp = [items[i]]
            
    if temp:
        result_list.append(temp)
    
    result_list = [sorted(i, reverse=True) for i in result_list]


    result = []
    for i in result_list:
        result += i

    return result



if __name__ == '__main__':
    print("Example:")
    print(reverse_ascending([1,1,2]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [10, 7, 5, 4, 8, 7, 2, 3, 1]
    assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]
    print("Coding complete? Click 'Check' to earn cool rewards!")

