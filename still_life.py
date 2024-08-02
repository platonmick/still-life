#!/usr/bin/env python3

"""
Charlotte is going to paint a still life, but first she has to set the scene.
She has the following eight items: red grapes, a bottle of red wine, a banana,
a sunflower, a green apple, a green vase, a pine cone and a wooden bowl.
From the following clues, can you determine which objects Caroline will select?
 
- She will pick exactly one fruit.
- She will pick the vase only if she also picks the sunflower.
- She will pick exactly two man-made objects, but only one made of glass.
- She will pick exactly one item of each color.
"""

from pysat.formula import CNF
from pysat.solvers import Solver
from time import time_ns


ITEMS = [
    "apple",
    "vase",
    "grapes",
    "wine",
    "banana",
    "sunflower",
    "pine cone",
    "bowl",
]
(
    apple,
    vase,
    grapes,
    wine,
    banana,
    sunflower,
    pine_cone,
    bowl,
) = (1, 2, 3, 4, 5, 6, 7, 8)

formula = CNF()

# at least one fruit ...
formula.append([grapes, banana, apple])

# ... but also not more than one
formula.append([-grapes, -banana])
formula.append([-grapes, -apple])
formula.append([-banana, -apple])

# if the vase is picked also pick the sunflower
formula.append([-vase, sunflower])

# pick exactly two man-made objects, ...
formula.append([vase, wine])
formula.append([vase, bowl])
formula.append([wine, bowl])
# ... but only one made of glass
formula.append([-vase, -wine])

# pick exactly one item of each color
formula.append([apple, vase])
formula.append([-apple, -vase])
formula.append([grapes, wine])
formula.append([-grapes, -wine])
formula.append([banana, sunflower])
formula.append([-banana, -sunflower])
formula.append([pine_cone, bowl])
formula.append([-pine_cone, -bowl])

# print resulting formula
print(
    " ∧ ".join(
        f"""({" ∨ ".join(("¬" if literal < 0 else "") + ITEMS[abs(literal) - 1] for literal in clause)})"""
        for clause in formula.clauses
    )
)


def calculcate_all_solutions():
    solutions = []
    while True:
        solver = Solver()
        solver.append_formula(formula)
        if not solver.solve():
            break
        model = solver.get_model()
        solution = [ITEMS[i - 1] for i in model if i > 0]
        solutions.append(solution)
        # Add clause to exclude the found solution
        formula.append([-i for i in model])
    return solutions

t0 = time_ns()
solutions = calculcate_all_solutions()
dt = time_ns() - t0
for solution in solutions:
    print(solution)

print(f"Calculation time: {dt / 1_000_000} ms")
