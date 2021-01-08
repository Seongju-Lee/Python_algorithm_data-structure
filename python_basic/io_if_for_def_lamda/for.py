scores = [90, 85, 77, 65, 91]
cheating = {2,4}

for i in range(len(scores)):
    if i + 1 in cheating:
        continue
    elif scores[i] > 80:
        print(i+1, "번째 합격")

