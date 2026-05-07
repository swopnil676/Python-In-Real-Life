data = [1,2,3,4,5,6,7,8,9]
nums = []
for i in data:
    if i%2 ==0 or i%3 ==0:
        if i%2 ==0:
            i /= 2
        else:
            i **= 3
        if i < 20:
            nums.append(i)
nums.sort()
print(nums)



# ✅ i = 1
# Not divisible by 2 or 3 → ❌ skip
# ✅ i = 2
# Divisible by 2 ✔
# i /= 2 → 2 / 2 = 1.0
# 1.0 < 20 ✔ → append

# 👉 nums = [1.0]

# ✅ i = 3
# Divisible by 3 ✔
# i **= 3 → 3³ = 27
# 27 < 20 ❌ skip
# ✅ i = 4
# Divisible by 2 ✔
# 4 / 2 = 2.0
# < 20 ✔ → append

# 👉 nums = [1.0, 2.0]

# ✅ i = 5
# Not divisible by 2 or 3 → ❌ skip
# ✅ i = 6
# Divisible by 2 ✔ (even though also divisible by 3, only first condition runs)
# 6 / 2 = 3.0
# < 20 ✔ → append

# 👉 nums = [1.0, 2.0, 3.0]

# ✅ i = 7
# Not divisible → ❌ skip
# ✅ i = 8
# Divisible by 2 ✔
# 8 / 2 = 4.0
# < 20 ✔ → append

# 👉 nums = [1.0, 2.0, 3.0, 4.0]

# ✅ i = 9
# Divisible by 3 ✔
# 9³ = 729
# < 20 ❌ skip