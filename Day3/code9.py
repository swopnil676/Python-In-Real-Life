text = input("Paste your long text here: ")

sentences = text.split('.')
# summary = sentences[0] + "..." + sentences[-1] # The last sentence is missing => Summary: Python is easy to learn...
summary = sentences[0] + "..." + sentences[-2] # gets the actual last sentence => Summary: Python is easy to learn... It is used in AI

print(f"Summary: {summary}")
print("\nSave Time")