# Date --> 4 December 2023   11:37
import re

a1 = input()
a = a1.lower()
# a = 'jodu kodu'
ans = re.sub("[aeiouy]", "", a) #replace
answer = '.'.join(ans)
print(f".{ans}")
