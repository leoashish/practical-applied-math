"""Practical Applied Math: modelling, dimensional analysis (Howison)."""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "visuals", "pam")
os.makedirs(OUT, exist_ok=True)


def buckingham_pi_example():
    # Drag force F = f(rho, v, L, mu). Pi groups: Cd = F/(0.5 rho v^2 L^2), Re = rho v L / mu.
    # Visual: plot Cd vs Re schematic
    Re = np.logspace(1, 6, 50)
    Cd = 24/Re + 0.5  # toy drag curve
    fig, ax = plt.subplots()
    ax.loglog(Re, Cd)
    ax.set_xlabel("Reynolds number Re")
    ax.set_ylabel("Drag coefficient Cd")
    ax.set_title("Dimensional analysis: drag curve")
    ax.grid(True, which="both")
    fig.savefig(os.path.join(OUT, "buckingham_pi.png")); plt.close(fig)


def nondim_example():
    # Nondim of falling body: y'' = -g, scale y=L, t=sqrt(L/g)
    t = np.linspace(0, 5, 200)
    y = 0.5 * 9.8 * t**2  # dimensional
    tn = t / np.sqrt(1/9.8)  # L=1
    yn = y / 1.0
    fig, ax = plt.subplots()
    ax.plot(t, y, label="dimensional")
    ax.plot(tn, yn, "--", label="nondimensional")
    ax.legend(); ax.grid(); ax.set_title("Nondimensionalisation")
    fig.savefig(os.path.join(OUT, "nondim.png")); plt.close(fig)


def run_all():
    buckingham_pi_example()
    nondim_example()
    print("modelling visuals done")
