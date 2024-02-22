def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid_index = (left + right) // 2
        mid_element = numbers[mid_index]

        if mid_element == target:
            return mid_index
        elif mid_element < target:
            left = mid_element + 1
        else:
            right = mid_element - 1

    return - 1


nums = [int(x) for x in input().split()]
target_num = int(input())
print(binary_search(nums, target_num))