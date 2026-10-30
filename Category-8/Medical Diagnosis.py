# Knowledge base: facts, rules, forward chaining and backward chaining.
# Educational symptom-rule demo only; not a medical diagnosis.
rules=[({"fever","cough"},"possible_flu"),({"sneezing","runny_nose"},"possible_allergy"),({"fever","sore_throat"},"possible_throat_infection")]
facts=set(input("Enter symptoms separated by commas: ").lower().replace(" ","").split(",")); facts.discard("")
def forward(known):
    result=set(known); changed=True
    while changed:
        changed=False
        for conditions,conclusion in rules:
            if conditions<=result and conclusion not in result:
                result.add(conclusion); print("Rule fired:",conditions,"->",conclusion); changed=True
    return result
def backward(goal,known,seen=None):
    if goal in known: return True
    seen=set() if seen is None else seen
    if goal in seen: return False
    seen.add(goal)
    return any(all(backward(c,known,seen.copy()) for c in conditions)
               for conditions,result in rules if result==goal)
derived=forward(facts)
print("Facts and inferred results:",sorted(derived))
for goal in ["possible_flu","possible_allergy","possible_throat_infection"]:
    print(goal,":",backward(goal,facts))
print("For education only. Ask a qualified healthcare professional about symptoms.")
