from pyomo.environ import *

# Capacidade do caminhão
W = 40  # Capacidade máxima de peso (em toneladas)
V_max = 50  # Capacidade máxima de volume (em metros cúbicos)

# Conjunto de grãos
grains = ['Milho', 'Soja', 'Feijão']

# Parâmetros para cada grão
rho = {'Milho': 0.75,  # Densidade (t/m³)
       'Soja': 0.70,
       'Feijão': 0.80}

v_max = {'Milho': 30,  # Volume máximo permitido pela legislação (m³)
         'Soja': 25,
         'Feijão': 20}

r = {'Milho': 200,  # Receita por metro cúbico ($/m³)
     'Soja': 250,
     'Feijão': 300}

# Criando o modelo
model = ConcreteModel()

# Definindo as variáveis de decisão
model.x = Var(grains, domain=NonNegativeReals)

# Função objetivo: maximizar a receita total
def objective_rule(model):
    return sum(r[i] * model.x[i] for i in grains)
model.profit = Objective(rule=objective_rule, sense=maximize)

# Restrição de capacidade de peso
def weight_constraint_rule(model):
    return sum(rho[i] * model.x[i] for i in grains) <= W
model.weight_constraint = Constraint(rule=weight_constraint_rule)

# Restrição de capacidade de volume
def volume_constraint_rule(model):
    return sum(model.x[i] for i in grains) <= V_max
model.volume_constraint = Constraint(rule=volume_constraint_rule)

# Restrições legislativas de volume máximo por grão
def legislative_constraints_rule(model, i):
    return model.x[i] <= v_max[i]
model.legislative_constraints = Constraint(grains, rule=legislative_constraints_rule)

# Resolvendo o modelo usando o solver GLPK
solver = SolverFactory('glpk')
result = solver.solve(model)

# Exibindo os resultados
print("Status da Otimização:", result.solver.status)
print("Condição de Término:", result.solver.termination_condition)
print("\nValores Ótimos das Variáveis:")
for i in grains:
    print(f"Quantidade de {i}: {model.x[i]():.2f} m³")

print(f"\nReceita Total: R$ {model.profit():.2f}")
