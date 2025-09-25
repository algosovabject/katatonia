import pyfiglet

print(pyfiglet.figlet_format("Code Against the Code"))

import random

errors = [
    ZeroDivisionError("Wait across the borderline"),
    ValueError("All the filth that soiled you, baby"),
    RuntimeError("The code against the code"),
    FileNotFoundError("Money going through the wire")
]

raise random.choice(errors)
