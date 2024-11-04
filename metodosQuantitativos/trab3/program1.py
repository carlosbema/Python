from pyomo.environ import *
import sys

def ler_trainees(arquivo):
    trainees_info = {}
    trainees_por_projeto = {
        'Driblando': set(),
        'SMART': set(),
        'PlanetHeroes': set(),
        'X4CHANGE': set()
    }
    trainees_com_alergia = set()
    
    try:
        with open(arquivo, 'r') as f:
            next(f)
            for linha in f:
                id_trainee, projeto, alergia = linha.strip().split('|')
                num_trainee = int(id_trainee[1:])
                trainees_por_projeto[projeto].add(num_trainee)
                if alergia == 'Sim':
                    trainees_com_alergia.add(num_trainee)
                trainees_info[num_trainee] = {
                    'projeto': projeto,
                    'alergia': alergia == 'Sim'
                }
        return trainees_info, trainees_por_projeto, trainees_com_alergia
    except:
        print("Erro ao ler arquivo de trainees")
        sys.exit(1)

def criar_matriz_tempos():
    return {
        (1,1): 30, (1,2): 18, (1,3): 65, (1,4): 32, (1,5): 54, (1,6): 64, (1,7): 77, (1,8): 35, (1,9): 74, (1,10): 77,
        (2,1): 43, (2,2): 48, (2,3): 60, (2,4): 13, (2,5): 44, (2,6): 58, (2,7): 55, (2,8): 53, (2,9): 49, (2,10): 67,
        (3,1): 93, (3,2): 79, (3,3): 49, (3,4): 69, (3,5): 76, (3,6): 27, (3,7): 62, (3,8): 45, (3,9): 52, (3,10): 39,
        (4,1): 80, (4,2): 88, (4,3): 35, (4,4): 49, (4,5): 63, (4,6): 40, (4,7): 44, (4,8): 53, (4,9): 34, (4,10): 29,
        (5,1): 102, (5,2): 99, (5,3): 20, (5,4): 68, (5,5): 48, (5,6): 11, (5,7): 33, (5,8): 68, (5,9): 22, (5,10): 24,
        (6,1): 67, (6,2): 64, (6,3): 42, (6,4): 49, (6,5): 78, (6,6): 34, (6,7): 65, (6,8): 25, (6,9): 44, (6,10): 42,
        (7,1): 107, (7,2): 111, (7,3): 34, (7,4): 80, (7,5): 67, (7,6): 48, (7,7): 36, (7,8): 79, (7,9): 39, (7,10): 71,
        (8,1): 68, (8,2): 70, (8,3): 38, (8,4): 40, (8,5): 57, (8,6): 46, (8,7): 36, (8,8): 57, (8,9): 28, (8,10): 60,
        (9,1): 95, (9,2): 105, (9,3): 48, (9,4): 70, (9,5): 39, (9,6): 54, (9,7): 58, (9,8): 75, (9,9): 29, (9,10): 56,
        (10,1): 79, (10,2): 88, (10,3): 32, (10,4): 54, (10,5): 47, (10,6): 40, (10,7): 30, (10,8): 79, (10,9): 23, (10,10): 54,
        (11,1): 61, (11,2): 54, (11,3): 50, (11,4): 53, (11,5): 64, (11,6): 42, (11,7): 57, (11,8): 44, (11,9): 53, (11,10): 50,
        (12,1): 89, (12,2): 95, (12,3): 32, (12,4): 59, (12,5): 41, (12,6): 33, (12,7): 41, (12,8): 65, (12,9): 13, (12,10): 49,
        (13,1): 73, (13,2): 61, (13,3): 35, (13,4): 71, (13,5): 63, (13,6): 27, (13,7): 48, (13,8): 33, (13,9): 39, (13,10): 44,
        (14,1): 74, (14,2): 86, (14,3): 20, (14,4): 51, (14,5): 44, (14,6): 27, (14,7): 17, (14,8): 79, (14,9): 18, (14,10): 47
    }

def resolver_alocacao(arquivo_trainees):
    trainees_info, trainees_por_projeto, trainees_com_alergia = ler_trainees(arquivo_trainees)
    n_trainees = len(trainees_info)
    
    model = ConcreteModel()
    
    n_hosts = 14
    n_ongs = 10
    tempos = criar_matriz_tempos()
    
    hosts_sem_animais = {6, 7, 8, 9, 10, 11, 12, 13, 14}
    hosts_com_animais = {1, 2, 3, 4, 5}
    
    ongs_por_projeto = {
        'Driblando': {1, 2, 3},
        'SMART': {4, 5, 6, 7},
        'PlanetHeroes': {8, 9, 10},
        'X4CHANGE': {8, 9, 10}
    }
    
    trainees_indices = list(trainees_info.keys())
    hosts_indices = list(range(1, n_hosts + 1))
    ongs_indices = list(range(1, n_ongs + 1))
    
    model.x = Var(hosts_indices, ongs_indices, trainees_indices, domain=Binary)
    
    model.obj = Objective(
        expr=sum(tempos[i,j] * model.x[i,j,k] 
                for i in hosts_indices 
                for j in ongs_indices 
                for k in trainees_indices),
        sense=minimize
    )
    
    def host_um_trainee_rule(model, i):
        return sum(model.x[i,j,k] for j in ongs_indices for k in trainees_indices) <= 1
    model.host_um_trainee = Constraint(hosts_indices, rule=host_um_trainee_rule)

    def trainee_uma_alocacao_rule(model, k):
        return sum(model.x[i,j,k] for i in hosts_indices for j in ongs_indices) == 1
    model.trainee_uma_alocacao = Constraint(trainees_indices, rule=trainee_uma_alocacao_rule)

    def capacidade_ong_rule(model, j):
        return sum(model.x[i,j,k] for i in hosts_indices for k in trainees_indices) <= 3
    model.capacidade_ong = Constraint(ongs_indices, rule=capacidade_ong_rule)

    def alergia_rule(model, k):
        if k in trainees_com_alergia:
            return sum(model.x[i,j,k] for i in hosts_com_animais for j in ongs_indices) == 0
        return Constraint.Skip
    model.alergia = Constraint(trainees_indices, rule=alergia_rule)

    def projeto_rule(model, k):
        projeto = trainees_info[k]['projeto']
        ongs_permitidas = ongs_por_projeto[projeto]
        return sum(model.x[i,j,k] for i in hosts_indices for j in ongs_permitidas) == 1
    model.projeto = Constraint(trainees_indices, rule=projeto_rule)

    solver = SolverFactory('glpk')
    results = solver.solve(model)
    
    if (results.solver.status == SolverStatus.ok and 
        results.solver.termination_condition == TerminationCondition.optimal):
        
        alocacoes = []
        tempo_total = 0
        
        for k in trainees_indices:
            for i in hosts_indices:
                for j in ongs_indices:
                    if value(model.x[i,j,k]) > 0.5:
                        tempo = tempos[i,j]
                        tempo_total += tempo
                        alocacoes.append((k, i, j, tempo))
        
        print("\nAlocações:")
        print("Trainee | Host | ONG | Tempo (min)")
        print("-" * 40)
        
        for k, i, j, tempo in sorted(alocacoes):
            print(f"T{k:02d}    | H{i:02d}  | O{j:02d} | {tempo:3d}")
        
        print(f"\nTempo total: {tempo_total} minutos")
        print(f"Tempo médio: {tempo_total/len(trainees_info):.2f} minutos")

if __name__ == "__main__":
    resolver_alocacao('trainees.txt')