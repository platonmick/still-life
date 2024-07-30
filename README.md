# Solve a logic puzzle with PySAT

[A post in the Subreddit "puzzles"](https://www.reddit.com/r/puzzles/s/uCq0PnahSw) stated the following puzzle:

    Charlotte is going to paint a still life, but first she has to set the scene.
    She has the following eight items: red grapes, a bottle of red wine, a banana,
    a sunflower, a green apple, a green vase, a pine cone and a wooden bowl.
    From the following clues, can you determine which objects Caroline will select?
 
    - She will pick exactly one fruit.
    - She will pick the vase only if she also picks the sunflower.
    - She will pick exactly two man-made objects, but only one made of glass.
    - She will pick exactly one item of each color.

Clarifications:

- Fruit: grapes, banana and apple.
- Man-made: bottle, vase and bowl.
- Red: grapes and wine.
- Green: apple and vase.
- Yellow: banana and sunflower.
- Brown: pine cone and bowl.

A puzzle of this kind is perfect to be solved by a SAT solver. That's a program that determines whether a given Boolean formula can be satisfied by assigning truth values to its variables, effectively finding solutions to complex logical problems.

You just have to transfer the rules given into constraints that can be fed into the solver and run it.

The Python script in [still_life.py](still_life.py) describes and solves the above puzzle. It uses [PySAT](https://pysathq.github.io/) to do so.
