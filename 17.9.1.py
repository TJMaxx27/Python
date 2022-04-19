array = [int(x) for x in input("Введите любое число в любом порядке, через пробел: ").split()]

def merge_sort(array):
    if len(array) < 2:
        return array[:]
    else:
        middle = len(array) // 2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result

print(merge_sort(array))


def binary_search(array, element):
    try:
        element = int(element)
    except ValueError:
        return
    if element not in array:
        return "Число выходит за пределы заданного списка"
    middle = len(array) // 2
    if array[middle] == element:
        try:
            return array[middle - 1], array[middle + 1]
        except IndexError:
            return array[middle - 1], array[middle]
    elif element > array[middle]:
        return binary_search(array[middle:], element)
    else:
        return binary_search(array[:middle + 1], element)

numbers = [i for i in range(1, 1001)]
user_numbers = int(input("Введите число от 0 до 999: "))
print(binary_search(numbers, user_numbers))
