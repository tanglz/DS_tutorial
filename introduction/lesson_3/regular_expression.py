# String Pattern Matching
# # The re module provides regular expression tools for advanced string processing.

# Test online tool : https://pythex.org/
# Further reading: https://docs.python.org/3/library/re.html#module-re

# \b Word boundary. This is a zero-width assertion that matches only at the beginning or end of a word.
import re
# w = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
# print(w)
# #
# # # # Simple patterns
# s = re.findall(r'test', 'This is a test sentence.')
# print(s)

# # special characters
# # metacharacter . ^ $ * + ? { } [ ] \ | ( )
# # # square brackets [ ], a set of characters
a = re.findall(r'[a-z]', 'Hello-world-123')
print(a)
# # # number of characters * {0,} + {1,} ? {0,1}
b = re.findall(r'\b[a-z]+', 'hello-world-123')
print(b)
# # # ^ not
c = re.findall(r'[^a-z0-9]+', 'hello-world-123')
print(c)
# # # $ match at the end of a line
d = re.findall(r'[a-zA-Z]+e$', 'Hello, Bree')
print(d)
# # # backslash \
# # # # remove special characters' special meaning, such as \*
b = re.findall(r'[a-z]+\*', 'Here are some metacharacters: (,[,and*')
print(b)
