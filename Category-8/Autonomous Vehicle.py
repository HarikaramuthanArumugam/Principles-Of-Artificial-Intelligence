# Knowledge base for a simplified autonomous vehicle decision system.
rules=[({"obstacle"},"stop"),({"red_light"},"stop"),({"pedestrian"},"stop"),
       ({"green_light","clear_road"},"move"),({"clear_road"},"safe_to_proceed_cautiously")]
facts=set(input("Enter sensor facts (comma-separated): ").lower().replace(" ","").split(",")); facts.discard("")
def forward(known):
    result=set(known); changed=True
    while changed:
        changed=False
        for conditions,conclusion in rules:
            if conditions<=result and conclusion not in result:
                result.add(conclusion); print("Rule:",conditions,"->",conclusion); changed=True
    return result
def backward(goal,known,seen=None):
    if goal in known: return True
    seen=set() if seen is None else seen
    if goal in seen: return False
    seen.add(goal)
    return any(all(backward(c,known,seen.copy()) for c in cond) for cond,out in rules if out==goal)
result=forward(facts)
print("Knowledge base:",sorted(result))
for goal in ["stop","move","safe_to_proceed_cautiously"]: print(goal,":",backward(goal,facts))
print("Vehicle decision:", "STOP" if "stop" in result else "MOVE" if "move" in result else "WAIT")
