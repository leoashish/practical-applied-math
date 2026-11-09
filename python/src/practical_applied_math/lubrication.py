"""Practical Applied Math: lubrication theory, thin films."""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "visuals", "pam")
os.makedirs(OUT, exist_ok=True)


def thin_film_visual():
    # h_t + (h^3 h_xxx)_x = 0 (simplified) - just show initial profile
    x = np.linspace(0, 10, 200)
    h = 1 + 0.3*np.sin(x)
    plt.plot(x, h)
    plt.title("Thin film height profile")
    plt.grid()
    plt.savefig(os.path.join(OUT, "thin_film.png")); plt.close()


def heat_bar_visual():
    # heat flow in bar of variable cross-section: (A(x) u_x)_x = 0
    x = np.linspace(0, 1, 50)
    A = 1 + 0.5*x  # cross section
    # solve (A u')' = 0 => A u' = const => u' = C/A => integrate
    C = 1.0
    uprime = C/A
    u = np.cumsum(uprime) * (x[1]-x[0])
    u = u - u[0]
    plt.plot(x, u, label="u(x)")
    plt.plot(x, A, label="A(x)")
    plt.legend(); plt.grid(); plt.title("Heat flow in variable cross-section bar")
    plt.savefig(os.path.join(OUT, "heat_bar.png")); plt.close()


def run_all():
    thin_film_visual()
    heat_bar_visual()
    print("lubrication visuals done")
