tc = int(input())
cards = list(map(int,input().split()))

s = 0
d = 0

l = 0
r = tc - 1
turn = True
while l <= r:
    if cards[l] > cards[r]:
        temp = cards[l]
        l += 1
    else:
        temp = cards[r]
        r -= 1

    if turn:
        s += temp
    else:
        d += temp

    turn = not turn

print(f"{s} {d}")




# if (cards.index(max(cards)) == 0) or (cards.index(max(cards)) == -1):
    #     tempS = max(cards)
    #     # print(tempS)
    #     s += tempS
    #     # print(s)
    #     cards.remove(max(cards))
    #     # print(cards)
    # if len(cards) == 0:
    #     break
    # if (cards.index(max(cards)) == 0) or (cards.index(max(cards)) == -1):
    #     tempD = max(cards)
    #     # print(tempD)
    #     d += tempD
    #     # print(d)
    #     cards.remove(max(cards))
    #     # print(cards)
    # if len(cards) == 0:
    #     flag = False
