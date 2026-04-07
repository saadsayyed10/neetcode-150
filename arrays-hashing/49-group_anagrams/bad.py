from collections import defaultdict

def badApproach(strs: list[str]) -> list[list[str]]:
    res = defaultdict(list)
    for s in strs:
        sortedS = ''.join(sorted(s))
        res[sortedS].append(s)
    return list(res.values())

strs = ["act","pots","tops","cat","stop","hat"]
print(f"Output: {badApproach(strs)}")