"""Practical Applied Math: ODEs, phase portraits."""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "visuals", "pam")
os.makedirs(OUT, exist_ok=True)


def euler_solve(f, y0, t):
    y = np.zeros(len(t)); y[0] = y0
    for i in range(len(t)-1):
        dt = t[i+1]-t[i]
        y[i+1] = y[i] + dt*f(t[i], y[i])
    return y


def rk4_solve(f, y0, t):
    y = np.zeros(len(t)); y[0] = y0
    for i in range(len(t)-1):
        dt = t[i+1]-t[i]
        k1 = f(t[i], y[i])
        k2 = f(t[i]+dt/2, y[i]+dt*k1/2)
        k3 = f(t[i]+dt/2, y[i]+dt*k2/2)
        k4 = f(t[i]+dt, y[i]+dt*k3)
        y[i+1] = y[i] + dt/6*(k1+2*k2+2*k3+k4)
    return y


def ode_solve_visual():
    f = lambda t, y: -0.5*y + np.sin(t)
    t = np.linspace(0, 10, 200)
    ye = euler_solve(f, 1.0, t)
    yr = rk4_solve(f, 1.0, t)
    fig, ax = plt.subplots()
    ax.plot(t, ye, label="Euler")
    ax.plot(t, yr, label="RK4")
    ax.legend(); ax.grid(); ax.set_title("ODE solvers")
    fig.savefig(os.path.join(OUT, "ode_solve.png")); plt.close(fig)


def phase_portrait_visual():
    # dx/dt = y, dy/dt = -x (harmonic oscillator)
    x = np.linspace(-3, 3, 20); y = np.linspace(-3, 3, 20)
    X, Y = np.meshgrid(x, y)
    U = Y; V = -X
    fig, ax = plt.subplots()
    ax.quiver(X, Y, U, V, alpha=0.6)
    # trajectory
    # manual integration
    dt = 0.05
    px, py = [2.0], [0.0]
    cx, cy = 2.0, 0.0
    for _ in range(200):
        nx = cx + dt*cy
        ny = cy + dt*(-cx)
        px.append(nx); py.append(ny)
        cx, cy = nx, ny
    ax.plot(px, py, "r")
    ax.set_aspect("equal"); ax.grid(); ax.set_title("Phase portrait")
    fig.savefig(os.path.join(OUT, "phase_portrait.png")); plt.close(fig)


def run_all():
    ode_solve_visual()
    phase_portrait_visual()
    print("ode visuals done")
