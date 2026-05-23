# Chained Method Calls in Python
# Chained method calls allow you to call multiple methods
# on an object in a single line, where each method
# operates on the result of the previous one.
# Reduces temporary variables
# Makes code shorter and expressive
# Useful for quick transformations

    # Syntax
# object.method1().method2().method3()

    # Example
def process_text(text):
    return text.strip().split()[-1].upper() if text.strip() else "No data"

print(process_text("  hello world  "))

    # Logic
# "  hello world  "
#         ↓ strip()
# "hello world"
#         ↓ split()
# ["hello", "world"]
#         ↓ [-1]
# "world"
#         ↓ upper()
# "WORLD"

# Output
# WORLD


# Real World Use
# Data cleaning pipelines
# String processing in APIs
# Log analysis
# Text transformations in NLP