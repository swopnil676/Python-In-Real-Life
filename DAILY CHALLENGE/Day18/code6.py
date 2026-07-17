data = ["Python","Java","C++","JS"]
res = ""
for i in data:
    res += i[-1]
print(res)


'''
teration	String (i)	Last Character (i[-1])	Accumulated Result (res)
1	        "Python"	    'n'	                    "n"
2	        "Java"	        'a'	                    "na"
3	        "C++"	        '+'	                    "na+"
4	        "JS"	        'S'	                    "na+S"
'''