# print() Secret Params — sep=, end=, file=, flush=

# print() is a built-in function used to display output.
# It has hidden parameters to control formatting and behavior.

# By default:
# • Adds space between values
# • Ends with a newline
# • Returns None

import sys
import time

# Syntax
# print(*objects, sep=' ', end='\n', file=None, flush=False)
# Example: 1) print("Hi", 10, True)
#          2) print("2025", "05", "08", sep="-")

# Example

for i in range(5):
    print(f"Loading {i}", end="\r", flush=True)
    time.sleep(1)

# print("Done")   # Output: Doneing 4
print("\rDone     ")    # Output: Doneing 4

# Example (file=)
print("Error message", file=sys.stderr) # stderr means error output stream.

# Real World Use
# Formatting logs and outputs
# Creating CSV/text formats
# Progress indicators
# Debugging (stderr)