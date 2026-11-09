"""Practical Applied Math: delta functions, Green's functions."""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "visuals", "pam")
os.makedirs(OUT, exist_ok=True)


def delta_approx_visual():
    x = np.linspace(-3, 3, 400)
    for eps in [1.0, 0.5, 0.1]:
        d = (1/(eps*np.sqrt(np.pi))) * np.exp(-x**2/eps**2)
        plt.plot(x, d, label=f"eps={eps}")
    plt.title("Delta function approximations")
    plt.legend(); plt.grid()
    plt.savefig(os.path.join(OUT, "delta.png")); plt.close()


def heaviside_visual():
    x = np.linspace(-3, 3, 400)
    H = np.where(x >= 0, 1.0, 0.0)
    plt.plot(x, H)
    plt.title("Heaviside step")
    plt.grid()
    plt.savefig(os.path.join(OUT, "heaviside.png")); plt.close()


def greens_function_visual():
    # 1D Poisson: -u'' = f, Green's G(x,xi)=min(x,xi) - x*xi on [0,1] (with BC 0)
    x = np.linspace(0, 1, 100)
    xi = 0.3
    G = np.where(x <= xi, x*(1-xi), xi*(1-x))
    plt.plot(x, G)
    plt.axvline(xi, color="r", linestyle="--")
    plt.title("Green's function for -u'' on [0,1]")
    plt.grid()
    plt.savefig(os.path.join(OUT, "greens.png")); plt.close()


def run_all():
    delta_approx_visual()
    heaviside_visual()
    greens_function_visual()
    print("distributions visuals done")
