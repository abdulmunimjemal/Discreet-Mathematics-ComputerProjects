'''
Given the truth values of the propositions p and q, find the
truth values of the conjunction, disjunction, exclusive or,
conditional statement, and biconditional of these propositions.
'''

def logical_operations(p: bool, q: bool) -> bool:
    conjuction = p and q
    disjunction = p or q
    exclusive_or = (p and not q) or (not p and q)
    conditional = (not p) or q
    biconditional = (p and q) or (not p and not q)
    
    return conjuction, disjunction, exclusive_or, conditional, biconditional
