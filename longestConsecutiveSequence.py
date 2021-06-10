# Longest consecutive sequence
# given an unsorted array of integers nums, return the length of the longest consecutive elements sequence

nums = [0, 3, 7, 2, 5, 8, 4, 4, 6, 0, 1]


def longestcs():
    new_nums = sorted(nums)
    print(new_nums)
    count = 0
    consecutive = 1
    while count < len(new_nums) - 1:
        i = new_nums[count]
        if i + 1 == new_nums[count + 1]:
            consecutive = consecutive + 1

        # print(consecutive)
        count = count + 1
    print(consecutive)