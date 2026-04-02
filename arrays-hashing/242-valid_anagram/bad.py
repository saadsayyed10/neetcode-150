s = "rat"
t = "tar"

p = "rac"
q = "qac"

def badApproach(s1: str, s2: str) -> bool:
    if(len(s1) != len(s2)):
        return False
    
    return sorted(s1) == sorted(s2)

print("Is an anagram:", badApproach(p, q))