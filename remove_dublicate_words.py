strr = "This is a sentence.this is a simple sentence with dublicate words "

strrWords = strr.split()

result = []

for char in strrWords:
    lowerstr = char.lower()
    if lowerstr not in result:
        result.append(char)

print(result)
