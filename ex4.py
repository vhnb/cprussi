name_employee = input('Digite o nome do funcionario:')
role = int(input('Qual seu cargo?: 1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário'))
base_salary = float(input('Digite seu salário base:'))
extra_hours = int(input('Digite suas horas extras trabalhadas:'))
total_abscence = int(input('Total de faltas no mes:'))
havebonusperformance = input('Recebeu bonus por desempenho? (s/n): ').strip().lower()

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
    return (base_salary * 0.0015) * extra_hours

def calc_discountperabsence(base_salary, total_abscence):
    return (base_salary * 0.002) * total_abscence

def calc_bonus(role, havebonusperformance):
    if havebonusperformance != 's':
        return 0
    bonus_table = {
        1: 1000,
        2: 500,
        3: 300,
        4: 100
    }
    return bonus_table.get(role, 0)

role_name = chose_role(role)
value_extrahour = calc_extra_hours(base_salary, extra_hours)
value_absence = calc_discountperabsence(base_salary, total_abscence)
value_bonus = calc_bonus(role, havebonusperformance)

total_additions = value_extrahour + value_bonus
total_discounts = value_absence
final_salary = base_salary + total_additions - total_discounts

print(f'\nResumo do salário de: {name_employee}')
print(f'Cargo: {role_name}')
print(f'Salário bruto: R${base_salary:.2f}')
print(f'Total de acréscimos (horas extras + bônus): R${total_additions:.2f}')
print(f'Total de descontos (faltas): R${total_discounts:.2f}')
print(f'Salário final: R${final_salary:.2f}')
