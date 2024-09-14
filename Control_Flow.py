for i in range(10):
    j = 10 * i + 1
    print(j , end=' ')

if 3 + 3 < 7:
    print("This should be printed.")
if 2 ** 8 != 256:
    print("This should not be printed.")

'''
Awhile loop also has a predicate. It is evaluated at the top of a block of
 code. If it evaluates to True, then the block is executed and then it repeats.
 The repetition continues until the predicate evaluate to False or until the
 code reaches a break statement.
'''

x = 1
while x<12:
    print(x)
    x = x + 1