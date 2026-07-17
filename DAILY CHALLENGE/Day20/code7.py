# Ques 1
arr = {1,2,2,3,3,3,4}
freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(f"Frequency count: {freq}")



# Ques 2
arr = {1,2,3,4}

total = 0

for num in arr:
    total += num

print(f"Sum : {total}")
