#!/usr/bin/env python3

"""
Beschreibung:

Andreas, Brunhilde, Cornelia und Daniel essen heute ihre Leibspeise; Jeder mag ein anderes Gericht: Zur Auswahl stehen Kartoffelsuppe, Labskaus, Maultaschen und Nudelauflauf; Wer bevorzugt welches Essen?
Hinweise:

Brunhilde mag keinen Nudelauflauf und Cornelia hasst Maultaschen
Andreas hat eine Schwäche für Labskaus.
Die Anfangsbuchstaben der Lieblingsgerichte von Cornelia und Daniel folgen im Alphabet unmittelbar aufeinander

"""


from pysat.formula import CNF
from pysat.solvers import Solver
from time import time_ns


PERSONEN = [
  "andreas",
  "brunhilde",
  "cornelia",
  "daniel"
]
(andreas, brunhilde, cornelia, daniel) = (0, 1, 2, 3)

GERICHTE = [
  "kartoffelsuppe",
  "labskaus",
  "maultaschen",
  "nudelauflauf"
]
(kartoffelsuppe, labskaus, maultaschen, nudelauflauf) = (0, 1, 2, 3)

def pair(person, gericht):
    return 4 * person + gericht + 1

formula = CNF()

# Jeder hat ein und nur ein Leibgericht
for person in range(4):
    formula.append([pair(person, gericht) for gericht in range(4)])
    for gericht in range(4):
        for gericht2 in range(4):
            if gericht2 != gericht:
                formula.append([-pair(person, gericht), -pair(person, gericht2) ])

# Jeder hat ein anderes Leibgericht
for gericht in range(4):
    formula.append([pair(person, gericht) for person in range(4)])

# Brunhilde mag keinen Nudelauflauf 
formula.append([ -pair(brunhilde,  nudelauflauf) ])

# Cornelia hasst Maultaschen
formula.append([-pair(cornelia,  maultaschen) ])

# Andreas hat eine Schwäche für Labskaus.
formula.append([pair(andreas, labskaus)])

# Die Anfangsbuchstaben der Lieblingsgerichte von Cornelia und Daniel
# folgen im Alphabet unmittelbar aufeinander
formula.append([pair(cornelia, maultaschen), pair(cornelia, nudelauflauf)])
formula.append([pair(daniel, maultaschen), pair(daniel, nudelauflauf)])

def calculcate_all_solutions():
    solutions = []
    while True:
        solver = Solver()
        solver.append_formula(formula)
        if not solver.solve():
            break
        model = solver.get_model()
        solution = [(PERSONEN[(i - 1) // 4], GERICHTE[(i - 1) % 4]) for i in model if i > 0]
        solutions.append(solution)
        # Add clause to exclude the found solution
        formula.append([-i for i in model if i % 4 != labskaus])
    return solutions

solutions = calculcate_all_solutions()
for solution in solutions:
    print(solution)
