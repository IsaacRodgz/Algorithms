# CodeFights

# @param s : string
# @return the first instance of a non-repeating character in it. If there is no such character, return '_'

def firstNotRepeatingCharacter(s):
    for c in s:
        if s.index(c) == s.rindex(c):
            return c
    return '_'
