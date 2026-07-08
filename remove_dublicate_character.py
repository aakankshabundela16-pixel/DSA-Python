str = "programmirng"
lowerstr = str.lower()

result = " "

for char in lowerstr:
  if char not in result:
    result += char
print(result)