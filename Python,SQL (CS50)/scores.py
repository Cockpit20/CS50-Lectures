scores = []
for i in range(3):
    score=int(input("Score: "))
    scores= scores + [score]
avg = sum(scores)/len(scores)
print(f"Average={avg}")