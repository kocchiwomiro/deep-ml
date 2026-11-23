import math

def softmax(scores: list[float]) -> list[float]:
    summed=0
    for num in range(len(scores)):
        summed+=math.exp(scores[num]-max(scores))
    result=[]
    for num in range(len(scores)):
        result.append(math.exp(scores[num]-max(scores))/summed)
    return result