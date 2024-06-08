# DATE ==> 8 June 2024
# AUTHOR ==> SUMONTO

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    n = 0

    parttern = ""
    for i in range(1,13):
        if (i == a or i == b):
            parttern += "1"
        elif (i == c or i == d):
            parttern += "0"
    
    print ("YES" if parttern == "0101" or parttern == "1010" else "NO")
            
