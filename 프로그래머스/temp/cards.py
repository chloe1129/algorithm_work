def solution(cards1, cards2, goal):
    card1 = []
    card2 = []
    for i in goal:
        if i in cards1:
            card1.append(i)
        if i in cards2:
            card2.append(i)

    if cards1 == card1 and cards2 == card2:
        return "Yes"
    return "No"


print(solution(["i", "water", "drink"], ["want", "to"],
      ["i", "want", "to", "drink", "water"]))
