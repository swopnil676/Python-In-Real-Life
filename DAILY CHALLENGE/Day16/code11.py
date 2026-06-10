def solve_puzzle(values):
    unique_values = set(values)
    
    if len(unique_values) != len(values):
        return "Duplicate values found"
        
    expected_sum = sum(range(1, len(values) + 1))
    actual_sum = sum(values)
    
    if actual_sum != expected_sum:
        return "Sequence is incorrect"
        
    return "Puzzle solved!"

# values = [1, 2, 3, 4, 5]
values = [1, 2, 3, 4, 6]

result = solve_puzzle(values)
print(result)
