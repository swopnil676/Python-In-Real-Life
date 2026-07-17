# Define the puzzle inputs
puzzle_numbers = [3, 7, 2, 5]

# Function to solve the puzzle
def solve_puzzle(numbers):
    numbers.sort()
    return sum(numbers[:3])

# Execute the function
result = solve_puzzle(puzzle_numbers)

# Output the result
print(f"Puzzle solved: {result}")