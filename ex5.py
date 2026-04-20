name = input('Digite o nome do cliente: ')
age = int(input('Digite a idade do cliente: '))
income = float(input('Digite a renda mensal: R$'))
loan = float(input('Valor do emprestimo: R$'))
installments = float(input('Número de parcelas: (3 a 24)'))

def approve(age, income, loan):
    if age < 18:
        return False
    if valor > renda * 20:
        return False
    return True

def set_rate(installments):
    if installments <= 6:
        return 0.05
    elif installments <= 12:
        return 0.08
    else:
        return 0.10
    
def calc_installments(loan, rate, installments):
    return loan * (rate * (1 + rate) ** parcelas) / ((1 + rate) ** installments - 1)

def calc_total(isntallment, installments):
    return isntallment * installments

def calc_fees(total, loan):
    return total - loan

if not approve(age, income, loan):
    print('emprestimo negado')
    if age < 18:
        print('motivo: cliente menor de idade')
    if valor > renda * 20:
        print('motivo: valor excede 20x a renda mensal')
else:
    rate: set_rate(installments)
    installments = calc_installments(loan, rate, installments)
    total = calc_total(isntallment, installments)
    fees = calc_fees(total, loan)
    
    print(f'\nemprestimo aprovado')
    print(f'nome: {name}')
    print(f'valor financiado: R${valor:.2f}')
    print(f'taxa de juros: {taxa * 100:.0f}% ao mês')
    print(f'valor da parcela: R$ {parcela:.2f}')
    print(f'total pago: R${total:.2f}')
    print(f'juros pagos: R${juros:.2f}')
