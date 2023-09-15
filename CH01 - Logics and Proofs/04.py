"""
Given the truth values of the propositions p and q in
fuzzy logic, find the truth value of the disjunction and
the conjunction of p and q (see Exercises 46 and 47 of
Section 1.1).
"""

def fuzzy_logic(p: float, q: float) -> float:
    if (p>1 or q>1 or p<0 or q<0):
        print("Wrong Values")
        return None
    
    disjunction = max(p,q) # (OR)
    conjunction = min(p,q)  # (AND)
    
    return disjunction, conjunction