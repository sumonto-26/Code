for _ in range(int(input())):
    a = input()
    if "po" in a[-3:]:
        print("FILIPINO")
    if "desu" in a[-5:] or "masu" in a[-5:] :
        print("JAPANESE") 
    if "mnida" in a[-6:]:
        print("KOREAN")