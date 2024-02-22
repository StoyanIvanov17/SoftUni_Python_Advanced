def insertion_sort(nums):
    for i in range(1, len(nums)):  # starting from 1 because 0 is the sorted part
        key = nums[i]  # we get a key because when we swap elements it'll be lost
        j = i - 1  # we take the last number out of the sorted part

        #  until we reach the start
        #  and until we reach a position that we can place the key
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]  # shifts the element
            j -= 1  # we move left

        nums[j + 1] = key


numbers = [int(x) for x in input().split()]
insertion_sort(numbers)
print(*numbers)
