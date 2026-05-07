import time

def printlyrics():
    lyrics = [
        "Sambhaal ke rakha wo phool mera tu",
        "Meri shayari mein zaroor raha tu",
        "Jo aankhon mein pyaari si duniya basaayi",
        "Wo duniya bhi tha tu, wo lamha bhi tha tu",
        "Haan, lagte hain mujhko ye kisse sataane",
        "Deta na dil mera tujhko bhulaane",
        "Adhoore se vaade, adhoori si raatein",
        "Ab hisse mein daakhil mere bas wo yaadein",

        "Rehna tha ban ke humdam tera",
        "Aise jaana hi tha, phir tu kyun thehra",
        "Ab na maane mera dil ke na tere qaabil",
        "Thi ik aarzu ki main kehta raha, par",
        
        "Tu aata nahin",
        "Sapno se jaata nahin",
        "Mil jaaye, kya hi baat thi",
        "Qaamil ho jaata wahin",
        "Jo bhi ho raaz tera",
        "Mujhko bataata nahin",
        "Mil jaaye, kya hi baat thi",
        "Qaamil ho jaata wahin"
    ]

    delays = [0.8,0.9,0.8,1,1.2,1.3,1.1,0.8,0.7,0.8,0.8,0.7,0.8,0.6,1,1.2,1.0,0.6,0.7,0.5]

    for i, line in enumerate(lyrics):
        for char in line:
            print(char, end='',flush=True)
            time.sleep(0.055)

        print() # next line
        time.sleep(delays[i])

printlyrics()      
