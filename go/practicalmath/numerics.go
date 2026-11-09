// Package practicalmath implements numerical methods from
// "Practical Applied Mathematics" (Howison): ODEs, PDEs, asymptotics.
package practicalmath

import (
	"fmt"
	"math"

	"mlfromscratch/mat"
)

// ---------- ODE solvers ----------

// Euler solves dy/dt = f(t,y) with step h.
func Euler(f func(float64, float64) float64, y0, t0, tf, h float64) []float64 {
	n := int((tf-t0)/h) + 1
	y := make([]float64, n)
	t := t0
	y[0] = y0
	for i := 1; i < n; i++ {
		y[i] = y[i-1] + h*f(t, y[i-1])
		t += h
	}
	return y
}

// RK4 solves dy/dt = f(t,y).
func RK4(f func(float64, float64) float64, y0, t0, tf, h float64) []float64 {
	n := int((tf-t0)/h) + 1
	y := make([]float64, n)
	t := t0
	y[0] = y0
	for i := 1; i < n; i++ {
		k1 := f(t, y[i-1])
		k2 := f(t+h/2, y[i-1]+h*k1/2)
		k3 := f(t+h/2, y[i-1]+h*k2/2)
		k4 := f(t+h, y[i-1]+h*k3)
		y[i] = y[i-1] + h/6*(k1+2*k2+2*k3+k4)
		t += h
	}
	return y
}

// ---------- PDE: 1D heat equation explicit ----------
func HeatEquation(alpha, L, T float64, nx, nt int) [][]float64 {
	dx := L / float64(nx-1)
	dt := T / float64(nt)
	r := alpha * dt / (dx * dx)
	u := make([][]float64, nt+1)
	for i := range u {
		u[i] = make([]float64, nx)
	}
	// initial sin(pi x)
	for j := 0; j < nx; j++ {
		x := float64(j) * dx
		u[0][j] = math.Sin(math.Pi * x)
	}
	for n := 0; n < nt; n++ {
		for j := 1; j < nx-1; j++ {
			u[n+1][j] = u[n][j] + r*(u[n][j+1]-2*u[n][j]+u[n][j-1])
		}
	}
	return u
}

// ---------- PDE: 2D Laplace (Jacobi) ----------
func Laplace(N, iters int) [][]float64 {
	u := make([][]float64, N)
	for i := range u {
		u[i] = make([]float64, N)
	}
	// BC top = 1
	for j := 0; j < N; j++ {
		u[N-1][j] = 1.0
	}
	for it := 0; it < iters; it++ {
		new := make([][]float64, N)
		for i := range new {
			new[i] = make([]float64, N)
			copy(new[i], u[i])
		}
		for i := 1; i < N-1; i++ {
			for j := 1; j < N-1; j++ {
				new[i][j] = 0.25 * (u[i+1][j] + u[i-1][j] + u[i][j+1] + u[i][j-1])
			}
		}
		u = new
	}
	return u
}

// ---------- Boundary layer example ----------
func BoundaryLayer(eps float64, n int) ([]float64, []float64) {
	x := make([]float64, n)
	y := make([]float64, n)
	for i := 0; i < n; i++ {
		x[i] = float64(i) / float64(n-1)
		y[i] = 1 - math.Exp(-x[i]/eps)
	}
	return x, y
}

// ---------- WKB amplitude ----------
func WKB(x []float64) []float64 {
	out := make([]float64, len(x))
	for i, v := range x {
		if v <= 0 {
			out[i] = 0
			continue
		}
		out[i] = 1 / math.Pow(v, 0.25)
	}
	return out
}

// ---------- Green's function 1D Poisson ----------
func Greens1D(n int) ([]float64, []float64) {
	x := make([]float64, n)
	G := make([]float64, n)
	xi := 0.3
	for i := 0; i < n; i++ {
		x[i] = float64(i) / float64(n-1)
		if x[i] <= xi {
			G[i] = x[i] * (1 - xi)
		} else {
			G[i] = xi * (1 - x[i])
		}
	}
	return x, G
}

// ---------- Print helpers ----------
func PrintSlice(name string, v []float64, max int) {
	fmt.Print(name, ": ")
	if len(v) > max {
		v = v[:max]
	}
	for _, val := range v {
		fmt.Printf("%.3f ", val)
	}
	fmt.Println()
}

func PrintMatrix(m [][]float64, maxr, maxc int) {
	r := len(m)
	if r > maxr {
		r = maxr
	}
	for i := 0; i < r; i++ {
		c := len(m[i])
		if c > maxc {
			c = maxc
		}
		for j := 0; j < c; j++ {
			fmt.Printf("%.3f ", m[i][j])
		}
		fmt.Println()
	}
}

var _ = mat.NewMatrix
