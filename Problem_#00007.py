from string import ascii_lowercase
letters = {}

for index, item in enumerate(ascii_lowercase, start=1):
    letters[index] = item

print(letters)


def num_encodings(s):
    if s.startswith("0"):
        return 0
    elif len(s) <= 1:
        return 1
    total = 0

    if int(s[:2]) <= 26:
        total += num_encodings(s[2:])
    
    total += num_encodings(s[1:])
    return total

print(num_encodings("111"))
    
