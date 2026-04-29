oxygen = True
carbon_dioxide = False

if oxygen and carbon_dioxide:
    print("Energy")
elif oxygen or carbon_dioxide:
    print("Partial")
else:
    print("No Energy")