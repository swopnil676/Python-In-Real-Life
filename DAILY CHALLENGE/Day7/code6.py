x = 0

for i in range(5):
    x += i
    if x > 5:
        break

else:
    x = 50

# for-else means: else runs ONLY when loop ends without break
print(x) # 6

# No break → else runs ✅
# Break occurs → else skipped ❌