# Usage of lambda func() in list
products = [("Laptop", 1000, 800), ("Phone", 600, 500), ("Tablet", 400, 300)]
sorted_products = sorted(products, key=lambda item: item[1] / item[2])
print(sorted_products)


print("\n")


# Usage of lambda func() in math

    # Question 1
data = [lambda x: x * i for i in range(4)]
result = [f(2) for f in data]
print(result) 
    # Workflow
# for i in range(4)
#        │
#        ├── lambda x: x*i
#        ├── lambda x: x*i
#        ├── lambda x: x*i
#        └── lambda x: x*i
#                 │
#         loop ends → i = 3
#                 │
#       all lambdas use i = 3
#                 │
#          f(2) = 2*3 = 6
#                 │
#       [6, 6, 6, 6]

    # Question 2
data = [lambda x, i=i: x * i for i in range(4)]
result = [f(2) for f in data]
print(result) # [0, 2, 4, 6]
    # Visual Workflow
# for i in range(4)
#    │
#    ├─ i=0 ──> lambda x, i=0: x*i
#    │
#    ├─ i=1 ──> lambda x, i=1: x*i
#    │
#    ├─ i=2 ──> lambda x, i=2: x*i
#    │
#    └─ i=3 ──> lambda x, i=3: x*i

# data
#  │
#  ├─ f1(2) → 2*0 = 0
#  ├─ f2(2) → 2*1 = 2
#  ├─ f3(2) → 2*2 = 4
#  └─ f4(2) → 2*3 = 6
#           │
#           ▼
#    [0, 2, 4, 6]
