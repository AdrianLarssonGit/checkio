from typing import Iterable


def compress(items: list) -> Iterable:
    final_list = []
    # Not super happy about this solution!
    try:
        final_list.append(items[0])
    except IndexError:
        return final_list

    for i in range(1, len(items)):
        if items[i - 1] != items[i]:
            final_list.append(items[i])

    return final_list


if __name__ == '__main__':
    print("Example:")
    print(list(compress([])))
