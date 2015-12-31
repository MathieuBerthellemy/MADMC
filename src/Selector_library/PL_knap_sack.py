from gurobipy import *

def get_knap_sack(table):
	model = _def_PL(table)
	model.write("pl.lp")
	
	output = []
	try:
		model.optimize()
		#print model.status
		print "X = ", [v.x for v in model.getVars()]
		output = [v.x for x in model.getVars()]
	except GurobiError:
		print ""

	return output

def _def_PL(table):
	"""
	Dresse le programme lineaire
	"""
	model = Model("KnapSack")  

	# DEF VARIABLES
	X = _add_var(model, table)
	# DEF CONSTANTS
	S = _get_constants(table)

	# ADD CONSTRAINTS
	_add_constraint(model, X, S, n, p)
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
	tmp = quicksum([xi*si for xi, si in zip(X, S)])
	model.setObjective(tmp, GRB.MINIMIZE)
	model.update()

def _add_constraint(model, X, S):
	tmp = quicksum([xi*si for xi, si in zip(X, S)])
	model.addConstr(tmp < 1/2 * sum(S))

def _get_constants(table):
	output = []

	ideal, nadir = table.get_ideal_nadir()
	
	omega = [x - y for x, y in zip(nadir, ideal)]
	epsilon = 0.0000001

	for key, x in self.table.rows.items():
		tmp = [abs(i - j)*w for i, j, w in zip(x, nadir, omega)]
		output.append(max(tmp) + epsilon*sum(tmp))

	return output