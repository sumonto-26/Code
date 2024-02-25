import math

def solve(n):
    if math.sqrt(n) == int(math.sqrt(n)) and n > 3:
        for i in range(2, int(math.sqrt(n))):
            if n % i == 0:
                return "NO"
        return "YES"
    
    else:
        return "NO"

def main():
    useless_input = int(input())
    numbers = list(map(int, input().split()))

    for num in numbers:
        ans = solve(num)
        print(ans)

if __name__ == "__main__":
    main()
