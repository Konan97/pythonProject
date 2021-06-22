# given n pairs of parentheses, write a function to generate all combination of well formed parentheses.
# ex: input = 3
# output = ["((()))", "(()())", "(())()", "()(())", "()()()"]
# 1, ()
# 2, (()), ()()
# 4, (((())))), ((()())), (())(()), ()()(()), ()(())(), (())()(),
# ()((())), ((()))(), ()()()()
import sys
print(sys.getrecursionlimit())

input = 3 # 5
output = []


def generateparentheses():
    def rec(left, right, stack, cand):
        if left == right == 0:
            output.append(cand)
            return

        if left > 0:
            rec(left - 1, right, stack - 1, cand + "(")
        if stack < 0 < right:
            rec(left, right - 1, stack + 1, cand + ")")

    rec(3, 3, 0, "")
    print(output)
    return output