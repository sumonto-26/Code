for _ in range(int(input())):
    n = int(input())
    
    if n == 1:
        print("##\n##")
    else:
        for i in range(n):
            for _ in range(2):
                for j in range(n):
                    if (i + j) % 2 == 0:
                        print("##", end="")
                    else:
                        print("..", end="")
                print()
