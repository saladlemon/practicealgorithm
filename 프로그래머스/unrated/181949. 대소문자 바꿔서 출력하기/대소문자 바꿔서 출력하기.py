str = input()
new = ""
for char in str:
    if char.isupper():
        new += char.lower()
    else:
        new += char.upper()
    

print(new)