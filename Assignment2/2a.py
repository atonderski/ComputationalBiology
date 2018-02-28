from sympy import symbols, solve, Matrix, simplify

u, v, a, b, Du, Dv = symbols("u, v, a, b, Du, Dv")
system = [
    a - (b + 1) * u + u ** 2 * v,
    b * u - u ** 2 * v
]
fixed_points = solve(system, [u, v])
print(fixed_points)

X = Matrix(system)
jacobian = X.jacobian([u, v])
print(jacobian)
eigenvals = jacobian.eigenvals()
print(eigenvals)
eigs = list(eigenvals.keys())
det = jacobian.det()
trace = jacobian.trace()

for fixed_u, fixed_v in fixed_points:
    eig1 = simplify(eigs[0].subs({u: fixed_u, v: fixed_v}))
    eig2 = simplify(eigs[1].subs({u: fixed_u, v: fixed_v}))
    print("EIGENVALUES: \n%s\n%s" % (eig1, eig2))
    dt = simplify(det.subs({u: fixed_u, v: fixed_v}))
    print("DETERMINANT: \n%s" % (dt))
    trc = simplify(trace.subs({u: fixed_u, v: fixed_v}))
    print("TRACE: \n%s" % (trc))

# det > 0
# trc < 0

# a**2 > 0
# -a**2 + b -1 < 0
# b < 1 + a**2

# w* = (u*, v*)
# w = w* + dw(r,t)
# D = [1 0, 0 Dv];
# d/dt(dw(r,t)) = J(w*)dw + laplace D dw
# ansatz dw(r,t) = T(t)R(r)dw0
# 1/T(t)*d/dt(T(t))*dw0 = J(w*)dw0 + laplace(R(r))/R(r)*D*dw0

# Solve T part:
# 1/T(t) * d/dt(T(t)) = lambda = const
# T(t) = T(0)e**(lambda*t)

# Solve R part
# laplace(R(r))/R(r) = -k^2 = const

# Reinsert solutions
# lambda * dw0 = J(w*)dw0 - k^2 D dw0
# dw0(lambda - J(w*) - k^2 D) = 0
# K(k) = J - k^2 D
# eigenvalues are given by:
# lambda^2 - trK*lambda + detK = 0
# at least one eigenvalue is unstable for at least one k if tr(K) > 0 or det(K) < 0
# but tr(K) is always  negative since trK = trJ -k^2trD and trJ has to be negative according to homogenous stability analysis
# so the remaining danger is det(K) < 0

# det(K) = det(J-k^2D) = dk^4 - k^2(dJ_11 + J_22) + det(J)
# det(J) > 0  gives the condition dJ_11 + J_22 > 0
# since tr(J) < 0 we need d!=1 J_11 and J_22 of opposite signs
# ... see lecture notes

u_star, v_star = fixed_points[0]
J = jacobian.subs({u: u_star, v: v_star})
print(J)
J = J.subs({a: 3, b: 8})
print(J)

dc = symbols("dc")
critical_equation = dc ** 2 * J[0, 0] ** 2 + 2 * dc*(J[0, 0] * J[1, 1] - 2 * J.det()) + J[1, 1] ** 2
sols = solve(critical_equation, [dc])
print(sols)
print([s.evalf() for s in sols])

for s in sols:
    print((s*J[0,0] + J[1,1]).evalf())