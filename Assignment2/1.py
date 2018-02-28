from sympy import symbols, solve, Matrix, simplify

S, I, a, b, c, K, D = symbols("S I a b c K D")
system = [
    b * (I + S) - c * S - S * (I + S) / K - a * S * I,
    -c * I - I * (I + S) / K + a * S * I
]
fixed_points = solve(system, [S, I])
print(fixed_points)

X = Matrix(system)
jacobian = X.jacobian([S, I])
print(jacobian)
eigenvals = jacobian.eigenvals()
print(eigenvals)

eigs = list(eigenvals.keys())

for fixed_S, fixed_I in fixed_points:
    eig1 = simplify(eigs[0].subs({S: fixed_S, I: fixed_I}))
    eig2 = simplify(eigs[1].subs({S: fixed_S, I: fixed_I}))
    print("EIGENVALUES: %s, %s" % (eig1, eig2))

# b>c