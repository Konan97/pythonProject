# a list of words
# "abc" is a predecessor of "abac"
# a word chain is a sequence of words
words = ["a", "b", "ba", "bca", "bda", "bdca"]
# words = ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]


def longeststringchain():
    words.sort(key = len, reverse = True)  # sort by length of strings
    memo = {}
    print(words)

    def rec(word):
        if word not in words: return 0
        if word in memo:
            return memo[word]
        else:
            mx = 0
            for i in range(len(words)):
                mx = max(mx, rec(word[:i] + word[i+1:])+1)
            memo[word] = mx

    for word in words:
        rec(word)

        print(memo)

