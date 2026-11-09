"""Practical Applied Math: PDEs (heat, wave, Laplace) via finite differences."""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "visuals", "pam")
os.makedirs(OUT, exist_ok=True)


def heat_equation_visual():
    # 1D heat eq u_t = alpha u_xx, explicit
    L = 1.0; T = 0.1; alpha = 0.01
    nx = 50; nt = 200
    dx = L/(nx-1); dt = T/nt
    r = alpha*dt/dx**2
    u = np.zeros((nt+1, nx))
    x = np.linspace(0, L, nx)
    u[0] = np.sin(np.pi*x)  # initial
    for n in range(nt):
        u[n+1, 1:-1] = u[n, 1:-1] + r*(u[n, 2:] - 2*u[n, 1:-1] + u[n, :-2])
        # BC zero
    fig, ax = plt.subplots()
    for n in [0, nt//4, nt//2, nt]:
        ax.plot(x, u[n], label=f"t={n*dt:.3f}")
    ax.legend(); ax.grid(); ax.set_title("Heat equation (explicit)")
    fig.savefig(os.path.join(OUT, "heat_eq.png")); plt.close(fig)


def wave_equation_visual():
    L = 1.0; T = 1.0
    nx = 100; nt = 200
    dx = L/(nx-1); dt = T/nt
    c = 1.0
    r = c*dt/dx
    u = np.zeros((nt+1, nx))
    x = np.linspace(0, L, nx)
    u[0] = np.sin(np.pi*x)
    # initial velocity zero => u[1] approx
    u[1, 1:-1] = u[0, 1:-1] + 0.5*r**2*(u[0, 2:] - 2*u[0, 1:-1] + u[0, :-2])
    for n in range(1, nt):
        u[n+1, 1:-1] = (2*u[n, 1:-1] - u[n-1, 1:-1]
                         + r**2*(u[n, 2:] - 2*u[n, 1:-1] + u[n, :-2]))
    fig, ax = plt.subplots()
    for n in [0, nt//4, nt//2, nt]:
        ax.plot(x, u[n], label=f"t={n*dt:.2f}")
    ax.legend(); ax.grid(); ax.set_title("Wave equation")
    fig.savefig(os.path.join(OUT, "wave_eq.png")); plt.close(fig)


def laplace_visual():
    # 2D Laplace: (u_{i+1,j}+u_{i-1,j}+u_{i,j+1}+u_{i,j-1}-4u_{ij})=0
    N = 40
    u = np.zeros((N, N))
    # BC: top=1
    u[-1, :] = 1.0
    for _ in range(500):
        u[1:-1, 1:-1] = 0.25*(u[2:, 1:-1]+u[:-2, 1:-1]+u[1:-1, 2:]+u[1:-1, :-2])
    fig, ax = plt.subplots()
    im = ax.imshow(u, cmap="hot", origin="lower")
    fig.colorbar(im); ax.set_title("Laplace equation (steady state)")
    fig.savefig(os.path.join(OUT, "laplace.png")); plt.close(fig)


def run_all():
    heat_equation_visual()
    wave_equation_visual()
    laplace_visual()
    print("pde visuals done")
