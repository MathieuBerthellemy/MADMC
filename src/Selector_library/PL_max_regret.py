from gurobipy import *

def max_regret(row, table, P=[]):
	"""
		Input:
			- P: [(xi, xj), ...] liste de contraintes, xi prefere a xj
			- x: une alternative dont on cherche a determiner le regret maximal
			- X: toutes les alternatives

		Output:
			- le regret maximal pour l'alternative x donnee en parametre
			- -1 si aucune solution
	"""
	model = _def_PL(P, row, table)
	model.write("pl.lp")
	
	output = -1
	try:
		model.optimize()
		#print model.status
		#print "W = ", [v.x for v in model.getVars()[1:]]
		output = model.getVars()[0].x
	except GurobiError:
		print ""

	return output

def _def_PL(P, row, table):
	"""
		Dresse le programme lineaire
	"""
	model = Model("MR")  

	# DEF VARIABLES
	r, W = _add_var(model, table.get_columns_count())
	# ADD CONSTRAINTS
	_add_constraints(model, W, r, P, row, table.rows)
	# SET OBJECTIVE FUNCTION
	_add_obj(model, r)

	model.setParam( 'OutputFlag', False )
	return model


def _add_var(model, nb_criteres):
	"""
		r: variable servant a lineariser la maximisation
		wi: variables servant a modeliser les poids affectes sur chaque critere
	"""
	r = model.addVar(vtype=GRB.CONTINUOUS, name="r")

	W = []
	for i in range(nb_criteres):
		W.append(model.addVar(vtype=GRB.CONTINUOUS, lb=0.0, ub=1.0, obj=0.0, name="w%d"% i))

	model.update()
	return r, W

def _add_obj(model, r):
	"""
		On cherche a maximiser r (dans l'optique de maximiser f(a)-f(b))
	"""
	model.setObjective(r, GRB.MAXIMIZE)
	model.update()


def _add_constraints(model, W, r, P, row, rows):
	_add_const_linearisation_max(model, W, r, row, rows)

	_add_const_P(model, P, W)

	_add_const_sum_W_eq_1(model, W)

	model.update()


def _add_const_linearisation_max(model, W, r, row, rows):
	"""
		pour toutes alternatives a differente de celle donnee en parametre x
		on veux maximiser f(a)-f(x)
	"""
	for key, current_row in rows.items():
		if current_row != row:
			minus = LinExpr();
			minus.add(_f(W, current_row), 1.0)
			minus.add(_f(W, row), -1.0)
			model.addConstr(r, GRB.LESS_EQUAL, minus)


def _add_const_P(model, P, W):
	for (a, b) in P:
		model.addConstr(_f(W, a), GRB.GREATER_EQUAL, _f(W, b) + 0.00001)


def _add_const_sum_W_eq_1(model, W):
	"""
		la somme des poids est equale a un
	"""
	s = quicksum(w for w in W)
	model.addConstr(s == 1, "sum wi = 1")

def _f(W, x):
	"""
		INPUTS:
			- x: une voiture
		OUTPUTS:
			- Expr: sum w_i*C_i^x
	"""
	obj = LinExpr();
	obj.addTerms(x, W)
	return obj




