faceCardDict = {'A':'E','K':'D','Q':'C','J':'B','T':'A'}

def detectHandType(hand):
    counts = [hand.count(card) for card in hand]
    if 5 in counts:
        return 5
    elif 4 in counts:
        return 4
    elif 3 in counts:
        if 2 in counts:
            return 3.5
        else:
            return 2.5
    elif counts.count(2) == 4:
        return 2
    elif 2 in counts: 
        return 1  
    else:
        return 0

def strength(hand):
    return (detectHandType(hand), [faceCardDict.get(card,card) for card in hand])

file = open("./trey_input.txt")

plays = []
for line in file.readlines():
    line = line.strip()
    if line != '':
        hand, bid = line.split()
        plays.append((hand, int(bid)))

file.close()

plays.sort(key = lambda play: strength(play[0]))

sum = 0
for rank, (hand, bid) in enumerate(plays, 1):
    sum += rank * bid

print(sum)