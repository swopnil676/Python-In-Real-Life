import time

sentences = "Pyrhon is fun!"

start = time.time()
input(sentences + "\nType this: ")

end = time.time()
print("Time taken: ", round(end-start, 2), "seconds")
