# Questions 1
from copy import deepcopy
user ={
    "name":"Alex",
    "skills":["Python"]
}
backup = deepcopy(user)
backup["skills"].append("AI")

print(user)
print(backup)


print("\n")


# Questions 2
user ={
    "name":"Alex",
    "skills":["Python"]
}
backup = user.copy()
backup["skills"].append("AI")

print(user)
print(backup)

'''
user
│
└── skills → ["Python"]

backup = user.copy()

user.skills ────┐
                │
backup.skills ──┘
                │
                ▼
           ["Python"]

append("AI")

                ▼
      ["Python", "AI"]

Both user and backup see the same list.
'''