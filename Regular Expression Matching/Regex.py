


def isMatch(s, p):
    if not p:
        return not s
    if len(p) == 1 or p[1] != '*':
        if not s or (s[0] != p[0] and p[0] != '.'):
            return False
        return isMatch(s[1:], p[1:])
    else:
        while s and (s[0] == p[0] or p[0] == '.'):
            if isMatch(s, p[2:]):
                return True
            s = s[1:]
        return isMatch(s, p[2:])

print(isMatch("aa", "a"))  # Output: False
print(isMatch("aa", "a*"))  # Output: True
print(isMatch("ab", ".*"))  # Output: True
