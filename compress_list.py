from typing import Iterable


def compress(items: list) -> Iterable:
    final_list = []
    try:
        final_list.append(items[0])
    except IndexError:
        return final_list
    for i in range(1, len(items)):
        if items[i-1] != items[i]:
            final_list.append(items[i])



    return final_list


if __name__ == '__main__':
    print("Example:")
    print(list(compress([])))

  #   # These "asserts" are used for self-checking and not for an auto-testing
  #   assert list(compress([
  # 5, 5, 5,
  # 4, 5, 6,
  # 6, 5, 5,
  # 7, 8, 0,
  # 0])) == [5, 4, 5, 6, 5, 7, 8, 0]
  #   assert list(compress([1, 1, 1, 1, 2, 2, 2, 1, 1, 1])) == [1, 2, 1]
  #   assert list(compress([7, 7])) == [7]
  #   assert list(compress([])) == []
  #   assert list(compress([1, 2, 3, 4])) == [1, 2, 3, 4]
  #   assert list(compress([9, 9, 9, 9, 9, 9, 9])) == [9]
