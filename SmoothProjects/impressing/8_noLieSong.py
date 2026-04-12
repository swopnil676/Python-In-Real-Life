import sys
import time

def no_lie_ultra_speed():
    timeline = [
        ("FEEL YOUR EYES, THEY ALL OVER ME...",2.05),
        ("DON'T BE SHY, TAKE CONTROL OF ME...",2.10),
        ("GET THE VIBE, IT'S GONNA BE LIT TONIGHT...",2.05),
        ("NO LIE, NO LIE, NO-OO-LIE!",2.20),
        ("HYPNOTIZED, PULL ANOTHER ONE...",2.10),
        ("IT'S ALRIGHT, I KNOW WHAT YOU WANT...",2.10),
        ("GET THE VIBE, IT'S GONNA BE LIT TONIGHT...",2.05),
        ("NO LIE, NO LIE, NO LIE!",2.0),
        
    ]
        # Clear screen (works in most terminals)
    print("\033[2j\033[H", end="")

    for line, duration in timeline:
        sys.stdout.write(f"\033[1;92m>>> {line}\033[0m\n")
        sys.stdout.flush()
        time.sleep(duration)

if __name__ == "__main__":
    time.sleep(0.3)
    no_lie_ultra_speed()