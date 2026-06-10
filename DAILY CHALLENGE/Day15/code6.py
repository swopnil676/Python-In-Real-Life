s1 = "Python makes programming easier"
print(" ".join(s1.split()[::-1]))

'''
"Python makes programming easier"   <- Original String
               │
               ▼  .split()
['Python', 'makes', 'programming', 'easier']   <- List of individual words
               │
               ▼  [::-1]
['easier', 'programming', 'makes', 'Python']   <- List reversed
               │
               ▼  " ".join()
"easier programming makes Python"   <- Final Output String
'''