"""Practical Applied Math: asymptotic expansions, boundary layers, WKB."""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "visuals", "pam")
os.makedirs(OUT, exist_ok=True)


def perturbation_visual():
    # epsilon expansion for sqrt(1+eps)
    eps = np.linspace(0, 0.5, 100)
    exact = np.sqrt(1+eps)
    p1 = 1 + eps/2
    p2 = 1 + eps/2 - eps**2/8
    plt.plot(eps, exact, "k", label="exact")
    plt.plot(eps, p1, "--", label="1st order")
    plt.plot(eps, p2, "--", label="2nd order")
    plt.legend(); plt.grid(); plt.title("Regular perturbation")
    plt.savefig(os.path.join(OUT, "perturbation.png")); plt.close()


def boundary_layer_visual():
    # (1-eps?) singular perturbation: eps y'' + y' = 0, y(0)=0,y(1)=1
    # outer: y~1; boundary layer near 0
    x = np.linspace(0, 1, 200)
    for eps in [0.1, 0.05, 0.01]:
        y = 1 - np.exp(-x/eps)
        plt.plot(x, y, label=f"eps={eps}")
    plt.legend(); plt.grid(); plt.title("Boundary layer")
    plt.savefig(os.path.join(OUT, "boundary_layer.png")); plt.close()


def wkb_visual():
    # WKB: y'' + (1/x) y = 0? Just plot oscillatory solution cos(1/eps * phi)
    x = np.linspace(0.1, 2, 400)
    eps = 0.05
    phi = x**1.5
    y = np.cos(phi/eps) / x**0.25
    plt.plot(x, y, alpha=0.7)
    plt.plot(x, 1/x**0.25, "r--", label="amplitude")
    plt.plot(x, -1/x**0.25, "r--")
    plt.legend(); plt.grid(); plt.title("WKB oscillatory")
    plt.savefig(os.path.join(OUT, "wkb.png")); plt.close()


def multiple_scales_visual():
    # amplitude modulation: cos(t) * (1 + 0.3 cos(0.1 t))
    t = np.linspace(0, 80, 2000)
    y = np.cos(t) * (1 + 0.3*np.cos(0.1*t))
    plt.plot(t, y, alpha=0.7)
    plt.plot(t, 1+0.3*np.cos(0.1*t), "r--")
    plt.plot(t, -(1+0.3*np.cos(0.1*t)), "r--")
    plt.title("Multiple scales: modulated oscillation")
    plt.grid()
    plt.savefig(os.path.join(OUT, "multiple_scales.png")); plt.close()


def run_all():
    perturbation_visual()
    boundary_layer_visual()
    wkb_visual()
    multiple_scales_visual()
    print("asymptotics visuals done")
