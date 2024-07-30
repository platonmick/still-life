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

solver = Solver()
solver.append_formula(formula)

if solver.solve():
    model = solver.get_model()
    print("Solution:")
    for i, item_idx in enumerate(
        [
            grapes,
            wine,
            banana,
            sunflower,
            apple,
            vase,
            pine_cone,
            bowl,
        ],
        start=1,
    ):
        if i in model:
            print(f"- {ITEMS[item_idx-1]}")
else:
    print("No solution found for the given constraints.")

