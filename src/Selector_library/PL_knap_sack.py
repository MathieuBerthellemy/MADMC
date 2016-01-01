from gurobipy import *

def get_knap_sack(table, column_poids, bounds):
	"""
		return the id of taken items
	"""
	model = _def_PL(table, column_poids, bounds)
	model.write("pl.lp")
	
	output = []
	try:
		model.optimize()
		#print model.status
		#print "X = ", [v.x for v in model.getVars()]
		output = [int(v.varName[1:]) for v in model.getVars() if v.x == 1]
		print output
		model.write("pl.sol")
	except GurobiError:
		print "ERROR"
	
	return output

def _def_PL(table, column_poids, bounds):
	"""
	Dresse le programme lineaire
	"""
	model = Model("KnapSack")  

	# DEF VARIABLES
	X = _add_var(model, table)
	# DEF CONSTANTS
	S = _get_constants(table)

	# ADD CONSTRAINTS
	_add_constraints(model, table, X, column_poids, bounds)
	# SET OBJECTIVE FUNCTION
	_set_obj(model, X, S)

	model.setParam( 'OutputFlag', False )
	return model

def _add_var(model, table):
	"""
		xi: prendre ou ne pas prendre l'objet i
	"""
	X = []
	for key, value in table.get_rows().items():
		X.append(model.addVar(vtype=GRB.BINARY, name="x%d"%key))

	model.update()
	return X

def _set_obj(model, X, S):
	tmp = quicksum([xi*1/si for xi, si in zip(X, S)])
	model.setObjective(tmp, GRB.MAXIMIZE)
	model.update()

def _add_constraint_poids(model, table, X, column_poids, values):
	tmp1 = quicksum([xi*ri[column_poids] for xi, ri in zip(X, values)])
	tmp2 = 0.5*sum([ri[column_poids] for ri in values])
	model.addConstr(tmp1 + 0.00001, GRB.LESS_EQUAL, tmp2)

def _add_constraint_cut(model, table, X, bounds, values):
	for i in range(len(bounds)):
		# MIN
		if table.direction[i] ==  False:
			tmp1 = quicksum([xi*ri[i] for xi, ri in zip(X, values)])
			tmp2 = bounds[i]
			model.addConstr(tmp1 + 0.00001, GRB.LESS_EQUAL, tmp2)
		# MAX
		if table.direction[i] ==  True:
			tmp1 = quicksum([xi*ri[i] for xi, ri in zip(X, values)])
			tmp2 = bounds[i]
			model.addConstr(tmp1, GRB.GREATER_EQUAL, tmp2 + 0.00001)

def _add_constraints(model, table, X, column_poids, bounds):
	v = table.get_rows().values()
	_add_constraint_poids(model, table, X, column_poids, v)
	_add_constraint_cut(model, table, X, bounds, v)

def _get_constants(table):
	output = []

	ideal, nadir = table.get_ideal_nadir()
	
	omega = [x - y for x, y in zip(nadir, ideal)]
	epsilon = 0.0000001

	for key, x in table.rows.items():
		tmp = [abs(i - j)*w for i, j, w in zip(x, nadir, omega)]
		output.append(max(tmp) + epsilon*sum(tmp))

	return output