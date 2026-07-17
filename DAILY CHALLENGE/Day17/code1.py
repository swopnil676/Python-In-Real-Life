text = input("Enter a text: ")
vowels = "aeiou"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Vowels: ",count)




# ASCII value finder :
char = input("Enter character : ")
print("ASCII value : ", ord(char))
# The built-in ord() function converts a single character into its underlying integer ASCII (or Unicode) code point value.