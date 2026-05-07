cars = ["Porsche","BMW","Audi"]
trending = []
for c in cars:
    if c == "BMW" or "Audi":
        trending.append(c)
print(trending) #['Porsche', 'BMW', 'Audi']


cars = ["Porsche","BMW","Audi"]
trending = []
for c in cars:
    if c in ["BMW", "Audi"]:
        trending.append(c)
print(trending) #['BMW', 'Audi']


cars = ["Porsche","BMW","Audi"]
trending = [c for c in cars if c in ["BMW", "Audi"]]

print(trending) #['BMW', 'Audi']