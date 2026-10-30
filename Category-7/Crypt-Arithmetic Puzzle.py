# Constraint satisfaction: solve SEND + MORE = MONEY.
from itertools import permutations
letters="SENDMORY"
for values in permutations(range(10),8):
    m=dict(zip(letters,values))
    if m["S"]==0 or m["M"]==0: continue
    send=1000*m["S"]+100*m["E"]+10*m["N"]+m["D"]
    more=1000*m["M"]+100*m["O"]+10*m["R"]+m["E"]
    money=10000*m["M"]+1000*m["O"]+100*m["N"]+10*m["E"]+m["Y"]
    if send+more==money:
        print("Letter assignments:")
        for letter in sorted(m): print(letter,"=",m[letter])
        print(f"{send} + {more} = {money}")
        break
else: print("No solution found.")
