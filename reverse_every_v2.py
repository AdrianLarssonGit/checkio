#After some thinking I got to this instead 
def reverse_ascending(items):
    # your code here
    result = []
    resultlist = []

    if not items:
        return resultlist

    temp = [items[0]]
    for i in range(1, len(items)):
        if items[i] > items[i-1]:
            temp.append(items[i])
        else:
            resultlist.append(temp)
            temp = [items[i]]
    if temp:
        resultlist.append(temp)
    resultlist = [sorted(i, reverse=True) for i in resultlist]
    
    print(resultlist)
    for i in resultlist:
        result += i

    return result


if __name__ == '__main__':
    print("Example:")
    print(reverse_ascending([1, 1, 2]))
