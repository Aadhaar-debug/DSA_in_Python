f = "a string"
g = ["my", "second", "favorite", "list"]
h = (1, "tuple")
i = {'a': 6, 'b': 77, 'c': 8}
j = {1,2,3,4,4,4,4,2,2,2,1}
print(len(f), len(g), len(h), len(i), len(j))

'''
For the sequential types (lists, tuples, and strings), you can slice a sub
sequence of indices using square brackets and a colon as in the following
 examples. The range of indices is half open in that the slice will start with
 the rst index and proceed up to but not including the last index. Negative
 indices count backwards from the end. Leaving out the rst index is the
 same as starting at 0. Leaving out the second index will continue the slice
 until the end of the sequence.
'''