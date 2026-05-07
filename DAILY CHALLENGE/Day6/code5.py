countries= ["America","Canada","India","Australia","China","Chile","California"]
for c in countries:
    if c.startswith("C"):
        countries.remove(c)
print(countries) #['America', 'India', 'Australia', 'Chile']


countries = ["America","Canada","India","Australia","China","Chile","California"]
countries = [c for c in countries if not c.startswith("C")]
print(countries) #['America', 'India', 'Australia']