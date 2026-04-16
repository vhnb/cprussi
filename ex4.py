name_employee = input('Digite o nome do funcionario:')
role = input('Qual seu cargo?: 1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário')
base_salary = float(input('Digite seu salário base:'))
extra_hours = int(input('Digite suas horas extras trabalhadas:'))
total_abscence = int(input('Total de faltas no mes:'))
havebonusperformance = input('Recebeu bonus por desempenho?: 1-Sim, 2-Não')

def verification_bonus():
    if havebonusperformance == 1:
        result_bonus = True
    elif havebonusperformance == 2:
        result_bonus = False
    else:
        return

def chose_role():
    if role == 1:
        role_chosen = 'Gerente'
    elif role == 2:
        role_chosen = 'Analista'
    elif role == 3:
        role_chosen = 'Assistente'
    elif role == 4:
        role_chosen = 'Estagiário'
    else:
        role_chosen = 'Cargo inválido'
        return

def calc_extra_hours(base_salary, extra_hours):
    value_extrahour = (base_salary * 0.0015) + extra_hours

def calc_discountperabsence(base_salary, total_abscence):
    value_absence = (base_salary * 0.002) + total_abscence

def calc_bonus(role, havebonusperformance):
    
