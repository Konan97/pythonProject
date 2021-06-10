# maximum product of word lengths
# given a string array words, return the maximum value of length(word[i]) * length(word[j]) where
# the two words do not share common letters.
from collections import defaultdict

words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]


def maxproductwordlength():
    nocommon = defaultdict(list)
    for w in words:
        nocommon[w] = list(w)
    print(nocommon)
    mx = 0
    for i in words:
        # print("i ", nocommon[i])
        for j in words:
            # print(nocommon[j])

            if bool(set(nocommon[j]) & set(nocommon[i])):
                continue
            else:
                mx = max(mx, len(i) * len(j))

    print(mx)


















