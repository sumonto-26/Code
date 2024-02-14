# my logic 
# date 29 december 2023

import re
a = input()
a = re.sub('144', 'a',a)
a = re.sub('14', 'b',a)
a = re.sub('1', 'c',a)
if a.isalpha() == True :
    print('YES')
else:
    print("NO")



# chat gpt
a = input()
a = a.replace('144', 'a').replace('14', 'b').replace('1', 'c')
print('YES' if a.isalpha() else "no")

