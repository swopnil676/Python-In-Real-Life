text = input("Enter a sentence: ")
words = text.split()
print("Number of word :",len(words))





student = {
    "marks": 85,
    "City": "Delhi"
}
print(student.get("marks"))
student.update({"marks": 90})
print(student)