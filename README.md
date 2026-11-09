# Practical Applied Mathematics (Howison)

Implementations and visual examples from *Practical Applied Mathematics:
Modelling, Analysis, Approximation* by Sam Howison. Separate from
"ML from scratch".

## Layout

```
practical_applied_math/
├── python/
│   ├── src/practical_applied_math/   # modelling, ODE, PDE, distributions, asymptotics, lubrication
│   ├── chapters/                     # one folder per book chapter (README + run.py)
│   ├── examples/applied_math_demo.py
│   └── visuals/pam/                  # generated PNGs
└── go/
    ├── practicalmath/                # numerical methods in Go
    └── chapters/                     # chapter folders
```

## Python

```bash
cd practical_applied_math/python
PYTHONPATH=. python examples/applied_math_demo.py   # generates visuals/pam/*.png
```

## Go

```bash
cd practical_applied_math/go
go build ./...
go run ./examples/practicalmath/   # if present
```

## Context
The book covers modelling, dimensional analysis, ODEs/PDEs, distributions,
asymptotic methods (perturbation, boundary layers, WKB, multiple scales),
and lubrication theory, with industrial case studies. Each chapter folder has
a README and a runnable visual demo.
EOF