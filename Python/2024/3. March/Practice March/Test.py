def p(text):
    print(text)
    
p(input())
p("Print anything with p()")
p(20)
p(type(20))

def sep(list, symbol):
    for i in range(len(list)):
        list[i] = str(list[i])
    ans = str(symbol).join(list)
    return ans

List = [1,2,3, 4,       5 ,   6]
p(sep(List, "+"))