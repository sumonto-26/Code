# DATE ==> 8 JUNE 2024
# AUTHOR ==> SUMONTO
a = input()
b = input()
c = input()
words = []
words.append(b[1]+a[0]+b[0])
words.append(a[2]+b[2]+c[2])
words.append(c[0]+b[1]+c[2])
words.append(a[0]+b[1]+c[2])
words.append(b[1]+c[1]+c[0])
for i in words:
    words.append(i[::-1])
    if len(words) == 10: break
print(min(words))

# Wrong Answer
# Wrong Answer
# Wrong Answer
# Wrong Answer
# Wrong Answer
# Wrong Answer
# Wrong Answer
# Wrong Answer
# Wrong Answer
# Wrong Answer
# Wrong Answer
# Wrong Answer
# Wrong Answer
# Wrong Answer
# Wrong Answer
# Wrong Answer
# Wrong Answer