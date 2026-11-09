"""Demo: practical applied mathematics (Howison) visuals."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.practical_applied_math.modelling import run_all as m
from src.practical_applied_math.ode import run_all as o
from src.practical_applied_math.pde import run_all as p
from src.practical_applied_math.distributions import run_all as d
from src.practical_applied_math.asymptotics import run_all as a
from src.practical_applied_math.lubrication import run_all as l

m(); o(); p(); d(); a(); l()
print("All applied math visuals generated in visuals/pam/")