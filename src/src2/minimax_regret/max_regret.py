from gurobipy import *

def MR(P, x, X):
	"""
		Input:
			- P1: [(xi, xj), ...] liste de contraintes, xi prefere a xj (maximisation)
			- x: une alternative
			- X: toutes les alternatives

		Output:
			- le regret maximal pour l'alternative x donnee en parametre
	"""
	model = _def_PL(P, x, X)
	model.write("pl.lp")
	model.optimize()

	for v in model.getVars():
		print v.varName, v.x

	return model.getVars()[0].x

def _def_PL(P, x, X):
	model = Model("MR")  

	# DEF VAR
	r, W = _add_var(model, 6)
	_add_constraints(model, W, r, P, x, X)
	_add_obj(model, r)

	return model


def _add_var(model, nb_criteres):
	r = model.addVar(vtype=GRB.CONTINUOUS, lb=0.0, ub=GRB.INFINITY, name="r")

	W = []
	for i in range(nb_criteres):
		W.append(model.addVar(vtype=GRB.CONTINUOUS, lb=0.0, ub=1.0, obj=0.0, name="w%d"% i))

	model.update()
	return r, W

def _add_obj(model, r):
	model.setObjective(r, GRB.MAXIMIZE)
	model.update()


def _add_constraints(model, W, r, P, x, X):
	_add_const_linearisation_max(model, W, r, x, X)

	_add_const_P(model, P)

	_add_const_sum_W_eq_1(model, W)

	model.update()


def _add_const_linearisation_max(model, W, r, x, X):
	for i in range(len(X)):
		if X[i] != x:
			minus = LinExpr();
			minus.add(_f(W, X[i]), 1.0)
			minus.add(_f(W, x), -1.0)
			model.addConstr(r <= minus, "r < f(y%d) - f(x)"%i)


def _add_const_P(model, P):
	for (a, b) in P:
		model.addConstr(_f(W, a) >= _f(W, b), "f(%d)>f(%d)"%(a.nom, b.nom))


def _add_const_sum_W_eq_1(model, W):
	s = quicksum(w for w in W)
	model.addConstr(s == 1, "sum wi = 1")

def _f(W, x):
	"""
		Input:
			- x: une voiture
		Output:
			- Expr: sum w_i*C_i^x
	"""
	obj = LinExpr();

	v = x.vectorize()

	obj.addTerms(v, W)

	return obj




