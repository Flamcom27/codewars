"""
find the maximum sum of a contiguous subsequence in list of integers

If the list is made up of only negative numbers, return 0 instead
"""
def max_sequence(arr):
    max_so_far = 0
    max_ending_here = 0
    for i in arr:
        max_ending_here = max_ending_here + i
        max_ending_here = max(max_ending_here, 0)
        max_so_far = max(max_so_far, max_ending_here) 
    return max_so_far


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
