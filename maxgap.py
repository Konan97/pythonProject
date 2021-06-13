# given an integer array nums, return the max difference between two successive elements
# in its sorted form.
from collections import defaultdict

input = [3, 6, 9, 1]


def maxgap():
    maxgap = 0
    if len(input) < 2:
        return 0
    else:
        # input.sort() # not linear time
        # bucket sorting
        low, high = min(input), max(input)
        bucket1 = defaultdict(list)
        for i in input:
            index = abs(low - i) * (len(input) - 1) // (high - low)
            bucket1[index].append(i)

        bucket2 = []
        for i in range(len(input)):
            if bucket1[i]:
                bucket2.append((min(bucket1[i]), max(bucket1[i])))
        print(bucket1)
        print(bucket2)

        difference = 0
        for i in range(len(input) - 1, 0, -1):
            difference = max(difference, input[i] - input[i-1])
        print(difference)
        return difference


