faceCardDict = {'A':'E','K':'D','Q':'C','J':'.','T':'A'}

def detectHandType(hand):
    jokers = hand.count('J')
    hand = hand.replace('J','')
    try:
        counts = list(set(hand.count(card) for card in hand))
        high = max(counts)
    except ValueError:
        high = 0    
    rank = 0
    secHigh = counts[-2] if len(counts) >= 2 else 0
    if high + jokers >= 5:
        rank = 5
    elif high + jokers >= 4:
        rank = 4
    elif high + jokers >= 3 and high + jokers + secHigh >= 5:
        rank = 3.5
    elif high + jokers >= 3:    
        rank = 2.5
    elif high + jokers >= 2 and secHigh + jokers + high >= 4:
        rank = 2
    elif high + jokers >= 2: 
        rank = 1  
    return rank

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