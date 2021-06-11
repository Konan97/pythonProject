# given a list of strings words and a string pattern, return a list of words[i]
# that match pattern.
# example: pattern = "abb" output = "mee" "aqq"

words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
pattern = "abb"

# convert pattern to numbers
# ex: "aaa" = "012", "abc" = "123", "122", etc.


def findreplacepattern():

    def convert(string):
        output = []
        lookup = {}  # dictionary to store the corresponding value of string
        i = 0
        for s in string:

            if s not in lookup:
                i += 1
                lookup[s] = i  # add value to the dictionary
                output.append(lookup[s])
            else:

                output.append(lookup[s])

        return output

    print(convert(pattern))
    end = []
    for word in words:
        if convert(word) == convert(pattern):
            end.append(word)
    print(end)
    return end







