from typing import List


def sorted_numbers(nums: List[int]):
    positives = sum(num for num in nums if num > 0)
    negatives = sum(num for num in nums if num < 0)

    print(negatives)
    print(positives)

    if positives > abs(negatives):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


numbers = [int(x) for x in input().split()]
sorted_numbers(numbers)
