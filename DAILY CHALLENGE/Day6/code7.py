empCur = ['Tom', 'Kevin', 'Richard']

empHist = empCur[:] #creates a shallow copy of the list.
empCur.append('Carla')

# That means empHist and empCur are two different lists in memory.
print(empHist)
print(empCur)