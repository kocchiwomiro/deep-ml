import math
from collections import Counter

def calculate_entropy(labels: list) -> float:
    """Calculate the entropy of a list of labels."""
    entropy=0
    counted=Counter(labels)
    for num in counted.values():
        entropy-=num*math.log(num,2)
    return entropy

def calculate_information_gain(examples: list[dict], attr: str, target_attr: str) -> float:
    """Calculate the information gain of splitting on attr."""
    focus=[row[target_attr] for row in examples]
    entropy=calculate_entropy(focus)
    split={}
    for data in examples:
        key=data[attr]
        if key not in split:
            split[key]=[]
        split[key].append(data)
    weights=0
    for sub in split.values():
        focus=[row[target_attr] for row in sub]
        subEnt=calculate_entropy(focus)
        weights-=len(sub)/len(examples)*subEnt
    return entropy+weights

def majority_class(examples: list[dict], target_attr: str) -> str:
    """Return the majority class. Break ties alphabetically."""
    focus=[row[target_attr] for row in examples]
    counted=Counter(focus)
    alphabet=dict(sorted(counted.items()))
    return max(alphabet,key=alphabet.get)

def learn_decision_tree(examples: list[dict], attributes: list[str], target_attr: str) -> dict:
    """Build a decision tree using the ID3 algorithm."""
    edge=[row[target_attr] for row in examples]
    if len(set(edge))==1:
        return edge[0]
    if not attributes:
        return majority_class(examples,target_attr)
    info=0
    best=attributes[0]
    for attr in attributes:
        gain=calculate_information_gain(examples,attr,target_attr)
        if info<gain:
            info=gain
            best=attr
    remain=[item for item in attributes if item!=best]
    focus=sorted(set([row[best] for row in examples]))
    branch={best: {}}
    for value in focus:
        sub=[row for row in examples if row[best]==value]
        if not sub:
            branch[best][value]=majority_class(examples,target_attr)
        else:
            branch[best][value]=learn_decision_tree(sub,remain,target_attr)
    return branch




