nums = [1,2,3,4,5,6,7]
new_list = []
for i in nums:
    if i%2 == 0:
        square = i**2
        if square<20:
            new_list.append(square)

    else:
        double=i*2
        if double<20:
            new_list.append(double)

print(new_list)