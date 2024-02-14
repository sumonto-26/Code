userday = int(input())
year = userday//365
userday= userday%365
month =userday//30
userday= userday%30
day = userday
print(f"{year} ano(s)")
print(f"{month} mes(es)")
print(f"{day} dia(s)")