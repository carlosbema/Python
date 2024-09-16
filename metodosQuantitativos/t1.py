from pyomo.environ import *

P = 200  # Peso máximo (toneladas)
V_max = 250  # Volume máximo (m³)

graos = ['Milho', 'Soja', 'Feijão']

densidade = {'Milho': 0.72,
       'Soja': 0.76,
       'Feijão': 0.7}

v_max = {'Milho': 100, 
         'Soja': 80,
         'Feijão': 90}

r = {'Milho': 200,  
     'Soja': 250,
     'Feijão': 180}

model = ConcreteModel()
model.x = Var(graos, domain=NonNegativeReals)

# Função objetivo
def func_objetivo(model):
    return sum(r[i] * model.x[i] for i in graos)

model.obj = Objective(rule=func_objetivo, sense=maximize)

# Restrições
def restricao_peso(model):
    return sum(densidade[i] * model.x[i] for i in graos) <= P

def restricao_volume(model):
    return sum(model.x[i] for i in graos) <= V_max

def restricao_legislacao(model, i):
    return model.x[i] <= v_max[i]

model.weight_constraint = Constraint(rule=restricao_peso)
model.volume_constraint = Constraint(rule=restricao_volume)
model.legislative_constraints = Constraint(graos, rule=restricao_legislacao)

# Solução
opt = SolverFactory('glpk')
opt.solve(model).write()
print("\nSOLUÇÃO ÓTIMA:")
for i in graos:
    print(f"Quantidade de {i}: {model.x[i]():.2f} m³")

print(f"\nReceita Total: R$ {model.obj():.2f}")
