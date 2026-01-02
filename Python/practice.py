import re
n = int(input())

pattern = re.compile(r"[+-]?(\d+)?\.\d+")

def validate(string):
    res = pattern.search(string)
    if res:
        return res.group(0) == string
    else:
        return False

for _ in range(n):
    string = input()
    print(validate(string))