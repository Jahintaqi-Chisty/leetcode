# def searchInsert(nums, target):
#         l,r = 0,len(nums)
#         while (l<=r):
#                 mid = l+((r-l)//2)
#                 if nums[mid]< target:
#                         l= mid+1
#                 elif nums[mid]> target:
#                         r = mid -1
#                 else:
#                         if nums[mid]== target:
#                                 return mid
#                         else:
#                                 return mid+1
                        


# numbers= [1]
# target=7
# result = searchInsert(numbers,target)

# print(f"The Position {result}")

from bigO import BigO
from random import randint

def quickSort(array):  # in-place | not-stable
    """
    Best : O(nlogn) Time | O(logn) Space
    Average : O(nlogn) Time | O(logn) Space
    Worst : O(n^2) Time | O(logn) Space
    """
    if len(array) <= 1:
        return array
    smaller, equal, larger = [], [], []
    pivot = array[randint(0, len(array) - 1)]
    for x in array:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)
    return quickSort(smaller) + equal + quickSort(larger)


lib = BigO()
complexity = lib.test(quickSort, "random")
complexity = lib.test(quickSort, "sorted")
complexity = lib.test(quickSort, "reversed")
complexity = lib.test(quickSort, "partial")
complexity = lib.test(quickSort, "Ksorted")