# min cost climbing stairs
# given an integer array cost where cost[i] is the cost of the ith step on a staircase.
# once you pay the cost, you can either climb one or two steps.

cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
cost = [10, 15, 20, 10]  # 25


def mincoststair():
    start0 = cost[0]
    start1 = cost[1]

    for i in range(2, len(cost)):
        tmp = cost[i] + min(start1, start0)
        start0 = start1
        start1 = tmp

    print(min(start1, start0))


