# Top k frequent element
    # 🔥Method 1
from collections import Counter

nums = [1,1,1,2,2,3]
k = 2
freq = Counter(nums)

result = [item for item , _ in freq.most_common(k)] 
#Get top k frequent => freq.most_common(k)
# item → number
# _ → frequency (ignored)
print(result)

    # 🔥Method 1
nums = [1,1,1,2,2,3]
k = 2

freq = {}

# count frequency
for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

# sort based on frequency
sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
# freq.items() => (number, frequency)
# key=lambda x: x[1] => Sort using frequency part.
# reverse=True => Descending order: largest frequency first.

# take top k
result = []
for i in range(k):
    result.append(sorted_items[i][0])
    # sorted_items[0] = (1,3) and [0] gets number → 1
    # sorted_items[1] = (2,2) and [0] gets number → 2

print(result) # Result becomes: [1, 2]