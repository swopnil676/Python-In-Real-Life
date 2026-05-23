# Packing / Unpacking Dicts — {**dict1, **dict2}

# Dictionary unpacking means spreading key-value
# pairs from one dictionary into another dictionary.
# {**dict1, **dict2} creates a NEW merged dictionary.
# If duplicate keys exist, the right-side value wins.

# Syntax
# merged = {**dict1, **dict2}

# Example
basic_info = {"name": "Alex", "city": "New York"}
job_info = {"role": "Software Engineer", "experience": "3 years"}
settings = {"theme": "dark"}

final_profile = {**basic_info, **job_info, **settings}

print(final_profile)

# Output
# {
#   'name': 'Alex',
#   'city': 'New York',
#   'role': 'Software Engineer',
#   'experience': '3 years',
#   'theme': 'dark'
# }

# Real World Use
# Combining API response data
# Merging default and custom settings
# Creating request payloads
# Updating user profiles