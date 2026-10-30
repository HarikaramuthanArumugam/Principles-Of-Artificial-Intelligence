# Manufacturing knowledge base using facts, rules and chaining.
rules=[({"machine_ready","material_available"},"production_can_start"),
       ({"production_can_start","temperature_ok"},"safe_to_manufacture"),
       ({"safe_to_manufacture","quality_passed"},"product_approved"),
       ({"defect_found"},"stop_production"),({"quality_passed"},"quality_verified")]
facts=set(input("Enter production facts separated by commas: ").lower().replace(" ","").split(",")); facts.discard("")
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
print("Facts and inferred results:",sorted(result))
for goal in ["production_can_start","safe_to_manufacture","product_approved","stop_production"]:
    print(goal,":",backward(goal,facts))
if "stop_production" in result: print("Decision: Stop line and inspect the defect.")
elif "product_approved" in result: print("Decision: Product approved by example rules.")
elif "safe_to_manufacture" in result: print("Decision: Manufacturing may proceed under example rules.")
else: print("Decision: More checks are required.")
