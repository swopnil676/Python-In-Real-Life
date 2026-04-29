text = input("Paste your long text here: ")

sentences = text.split('.')
summary = sentences[0] + "..." + sentences[-1]

print(f"Summary: {summary}")
print("\nSave Time")