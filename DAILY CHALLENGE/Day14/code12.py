class Bank:
    def __init__(self):
        self.bank_name = "Global Bank"
        self._branch_code = 1234
        self.__vault_password = "Secret_Password_123"

    def display_members(self):
        print(f"Inside Class - Name: {self.bank_name}")
        print(f"Inside Class - Branch: {self._branch_code}")
        print(f"Inside Class - Vault: {self.__vault_password}")


obj = Bank()
obj.display_members()

print("\n--- Outside Access ---")
print(f"Public: {obj.bank_name}")
print(f"Protected: {obj._branch_code}")
# print(f"Private: {obj.__vault_password}")  In Python, a variable starting with double underscore (__) is treated as private.


'''
Bank Object
│
├── bank_name           (public)
│      ↓
│   Accessible everywhere
│
├── _branch_code        (protected)
│      ↓
│   Accessible, but intended for internal use
│
└── __vault_password    (private)
       ↓
   Name-mangled to
   _Bank__vault_password
       ↓
   Direct access blocked
'''
