scores=list()
score=int(input("score="))
while score>=0:
    scores.append(score) 
    score=int(input("score="))
print("總列是:",scores)
print("總分是:",sum(scores))