"""Reverse a string of words without using native methods. Test corner cases & edge cases."""


def reverse_words(long_string):
    # store in array
    final = ""
    a = long_string.split(" ")
    for word in range(0, len(a)-1, -1):
        final += word + " "
    return final
    #final = ""
    # read and split at spaces
    # for c in long_string:
    #     if c == " ":       # From reverse, if encountered a space
    #         sliced = long_string.in    # strip until the space
    #         balance = long_string[:i]   # update balance string
    #         long_string = balance
    #         final.join(sliced)          # join to main string as reversed
    #         print("string joined..")
    # print(final)

# Driver code
print(reverse_words("Sky is Blue"))

#s = "Monday comes before Tuesday"
#print(s.split(" "))

