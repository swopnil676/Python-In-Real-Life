# Detected cycle in linked list:
nums = [1,2,3,4,2]
seen = set()
for n in nums:
    if n in seen:
        print("Cycle detected and duplicate is :",n)
    seen.add(n)