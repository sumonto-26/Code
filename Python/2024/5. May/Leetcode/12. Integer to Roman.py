# DATE ==> 10 May 2024
# AUTHOR ==> SUMONTO.

# num <= 3999
num = int(input())
arr = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1,
}
ans = ""
for i,j in arr.items():
    while(j <= num):
        ans += i
        num -= j
        
print(ans)