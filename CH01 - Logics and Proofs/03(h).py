import itertools

"""
h - hard
Give a compound proposition, determine whether it is satisfiable 
by checking its truth value for all positive assignments of truth 
values to its propositional variables
"""

# Function to evaluatie compound propositon - comp_proposition
def eval_propositions(expression: str, variable_assignment: dict) -> bool:
    for var, value in variable_assignment.items():
        expression = expression.replace(var, str(value))
    return eval(expression)


def is_satisfiable(comp_proposition):
    variables = set(var for car in comp_proposition if var.isalpha())
    possible_assignments = list(itertools.product([True, False], repeat=len(variables)))
    
    satisfiable = False
    for assignment in possible_assignments:
        variable_assignment = dict(zip(variables, assignment))
        result = eval_propositions(comp_proposition, variable_assignment)
        if result:
            satisfiable = True 
            break
    return satisfiable