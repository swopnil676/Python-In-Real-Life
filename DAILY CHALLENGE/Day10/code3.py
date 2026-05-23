try:
    spell = 1 / 0
except:
    print("Fail")
# except ZeroDivisionError:
#     print("Cannot divide by zero")

'''
Start
  ↓
Enter try block
  ↓
Execute: 1 / 0
  ↓
ZeroDivisionError occurs
  ↓
Python stops remaining try code
  ↓
Jump to except block
  ↓
Print "Fail"
  ↓
End
'''