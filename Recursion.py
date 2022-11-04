def fatorial(n):  # Big O - O(n)
    result = 1
    for i in range(n - 1):
        result = result * (n - i)
    return result


def fatorial_with_recursion(n):  # Big O - O(n)
    if n == 1:
        return n
    return n * fatorial_with_recursion(n - 1)


def binary_search(elem, array):  # Big O - O(n)
    founded = False
    while not founded:
        mid = (len(array) - 1) // 2
        if len(array) == 1:
            return "Not founded"
        if elem == array[mid]:
            founded = True
        elif elem > array[mid]:
            array = array[mid + 1:]
        else:
            array = array[:mid]
    return True


def binary_search_with_recursion(elem, min, max, array):
    pass


if __name__ == '__main__':
    print(fatorial(2))
    print(fatorial_with_recursion(4))

    lista = [1, 2, 3, 4, 5, 6, 7]
