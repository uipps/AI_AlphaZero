
cubestring = 'FFBLBRDLDUBRRFDDLRLUUUFB'  # cube definition string of cube we want to solve
# See module enums.py for the format of the cube definition string

import solver as sv
a = sv.solve(cubestring)
print(a)
