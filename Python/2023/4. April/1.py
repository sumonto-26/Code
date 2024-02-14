def funcation(n):
    if (n==1):
        return 1
    else:
        return n * funcation(n-1)

print( funcation (9))