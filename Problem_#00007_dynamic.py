from collections import defaultdict

def num_encodings(s):
    cache = defaultdict(int)
    cache[len(s)] = 1
    for i in reversed(range(len(s))):
        if s[i].startswith('0'):
            cache[i] = 0
        elif i == len(s) - 1:
            cache[i] = 1
        else:
            if int(s[i:i + 2]) <= 26:
                cache[i] =cache[i + 2]
            cache[i] += cache[i + 1]
    return cache[0]

print(num_encodings('001'))