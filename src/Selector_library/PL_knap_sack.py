from gurobipy import *
import time

def get_knap_sack(table, column_poids):
	"""
		return the id of taken items
	"""
	# table.unset_row(0)
	# table.unset_row(1)
	# table.unset_row(2)
	# table.unset_row(3)
	# table.unset_row(4)
	# table.unset_row(5)
	# table.unset_row(6)
	# table.unset_row(7)
	# table.unset_row(8)
	# table.unset_row(9)
	# table.unset_row(10)
	# table.unset_row(11)
	# table.unset_row(12)
	# table.unset_row(13)
	# table.unset_row(14)


	model = _def_PL(table, column_poids)
	model.write("pl.lp")
	
	output = []

	t1 = time.time()
	model.optimize()
	t2 = time.time()
	model.write("pl.sol")
	print t2 - t1
	#print model.status
	#print "X = ", [v.x for v in model.getVars()]
	output = [int(v.varName[1:]) for v in model.getVars() if v.x == 1]
	print output
	
	
	return output

def _def_PL(table, column_poids):
	"""
	Dresse le programme lineaire
	"""
	model = Model("KnapSack")  

	# DEF VARIABLES
	X = _add_var(model, table)
	# DEF CONSTANTS
	S = _get_constants(table)

	# ADD CONSTRAINTS
	_add_constraints(model, table, X, column_poids)
	# SET OBJECTIVE FUNCTION
	_set_obj(model, X, S)

	model.setParam('OutputFlag', False)
	return model

def _add_var(model, table):
	"""
		xi: prendre ou ne pas prendre l'objet i
	"""
	X = []
	for key, value in table.get_rows(False).items():
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
	model.addConstr(tmp1, GRB.LESS_EQUAL, tmp2 - 0.00001, "POIDS")

def _add_constraint_cut(model, table, X, values):
	for i in range(table.get_columns_count()):
		if table.columns_validity[i]:
			# MIN
			if table.direction[i] ==  False:
				tmp1 = quicksum([xi*ri[i] for xi, ri in zip(X, values)])
				tmp2 = table.bounds[i]
				model.addConstr(tmp1, GRB.LESS_EQUAL, tmp2 - 0.00001, "COL_%d"%i)
			# MAX
			if table.direction[i] ==  True:
				tmp1 = quicksum([xi*ri[i] for xi, ri in zip(X, values)])
				tmp2 = table.bounds[i]
				model.addConstr(tmp1, GRB.GREATER_EQUAL, tmp2 + 0.00001, "COL_%d"%i)

def _add_constraints(model, table, X, column_poids):
	v = table.get_rows(bounded=False).values()
	_add_constraint_poids(model, table, X, column_poids, v)
	_add_constraint_cut(model, table, X, v)

def _get_constants(table):
	output = []
	ideal, nadir = table.get_ideal_nadir()
	
	omega = [x - y for x, y in zip(nadir, ideal)]
	epsilon = 0.0000001
	
	for key, x in table.rows.items():
		tmp = [abs(i - j)*w for l, (i, j, w) in enumerate(zip(x, nadir, omega)) if table.columns_validity[l]]
		output.append(max(tmp) + epsilon*sum(tmp))

	return output