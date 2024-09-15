'''
 The word encapsulation has two di erent, but related, meanings. The
 rst is the idea of encapsulating or combining into a single thing, data and
 the methods that operate on that data. In Python, this is accomplished via
 classes, as we have seen.
 The second meaning of encapsulation emphasizes the boundary between
 the inside and the outside of the class, specifying what is visible to the users
 of a class. Often this means partitioning the attributes into public and
 private. In Python, there is no formal mechanism to keep one from access
ing attributes of a class from outside that class. So, in a sense, everything
 is public. However, there is a convention to make it clear what ought to
 be kept private. Any attribute that starts with an underscore is considered
 private. Think of it like someones unlocked diary. You can read it, but you
 shouldnt.
'''

class Diary:
    def __init__(self,title):
        self.title = title
        self._entries = [] # '_entries' this is how you declare a private variable or function
    def adfentry(self,entry):
        self._entries.append(entry)
