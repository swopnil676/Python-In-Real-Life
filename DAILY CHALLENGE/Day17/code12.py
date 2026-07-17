def solve_puzzle(data):
    n = len(data)
    result = []
    
    for i in range(n):
        if data[i] % 2 == 0:
            result.append(data[i] ** 2)
        else:
            result.append(data[i] ** 3)
            
    return result

data = [1, 2, 3, 4, 5]
solution = solve_puzzle(data)
print(solution)