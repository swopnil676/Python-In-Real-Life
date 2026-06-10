# exec() and eval() - Run Python Code Stored as a String
# eval() and exec() are built-in Python functions
# used to run Python code written as a string.
# eval() -> runs one expression and returns the result
# exec() -> runs multiple statements and returns None

# ⚠️ Never use eval() or exec() with user input (security risk)

# Syntax
# eval(expression_string)

# exec(code_string)

# With restricted scope:
# eval(expression, globals, locals)
# exec(code, globals, locals)

# Example
price = 200
discount = 0.10

formula = "price - (price * discount)"

final_price = eval(formula)

print("Final price:", final_price)

# Real World Use
# Calculator apps
# Dynamic formula engines
# Automation scripts
# Testing tools