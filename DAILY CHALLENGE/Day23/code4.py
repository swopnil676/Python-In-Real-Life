# Scenario:
# You receive a CSV file from a client 
# with inconsistent column names:

columns = [
    "Customer ID",
    "Customer Name",
    "Order Date",
    "Product Price($)"
]

# You need to standardize these column names 
# using List comprehension

new_columns = [
    col.lower().replace(" ", "_").replace("($)", "")
    for col in columns
]

print(new_columns)