from pyomo.environ import *

model = ConcreteModel()

model.x1 = Var(domain = NonNegativeReals)
model.x2 = Var(domain = NonNegativeReals)

# Função objetivo
def objective_function(model):
    return 1500 * model.x1 + 1000 * model.x2

# Definindo a o objetivo da função
model.obj = Objective(rule = objective_function, sense = maximize)

# Definindo as restrições
def amount(model):
    return model.x1 + model.x1 <= 30

def max_x1(model):
    return model.x1 >= 10

def max_x2(model):
    return model.x1 >=10

model.con1 = Constraint(rule = amount)
model.con2 = Constraint(rule = max_x1)
model.con3 = Constraint(rule = max_x2)

opt = SolverFactory('glpk')
opt.solve(model).write()

print('\n\nSOLUÇÃO ÓTIMA')
print('x1:', model.x1())
print('x2:', model.x2())
print('Objetivo:', model.obj())



