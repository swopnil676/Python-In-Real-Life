data = ["hello",9,"namaste",8,5,6,"friend",2,"PyQuestHub"]
refine = [str(d) for d in data]
print(data)

square = [int(r) for r in refine if r.isdigit()]
print(square) #[9, 8, 5, 6, 2]