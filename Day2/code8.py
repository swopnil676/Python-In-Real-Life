# if __name__ == "__main__" in Python
# This is a special condition used to check whether a Python file is being run directly or imported as a module.

# Every Python file has a built-in variable called __name__.
# When the file is run directly -> __name__ == "__main__"
# When imported -> __name__ == "filename"

# Syntax
# if __name__ == "__main__":
#     code to execute when run directly

# Example
def add(a, b):
    return a + b


def main():
    print("Sum:", add(5, 3))


if __name__ == "__main__":
    main()

# Real World Use
# Building reusable Python modules
# Writing test scripts
# Running scripts safely
# Large projects with multiple files