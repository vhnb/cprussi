digiteOrigemCarga = int(input("digite o cargo da origem de 1 a 5:"))
peso = int(input("digite o peso em tonelada:"))
codCarga = int(input("digite o codigo do cargo de 10 a 40:"))

pesokg = peso * 1000


if digiteOrigemCarga == 1:
    imposto = 0.35
elif digiteOrigemCarga == 2:
    imposto = 0.25
elif digiteOrigemCarga == 3:
    imposto = 0.15
elif digiteOrigemCarga == 4:
    imposto = 0.05
elif digiteOrigemCarga == 5:
    imposto = 0

if 10 <= codCarga <= 20:
    preço = 100
elif 21 <= codCarga <= 30:
    preço = 250
elif 31 <= codCarga <= 40:
    preço = 340


preçototal = pesokg * preço

valor_imposto = preçototal * imposto
valortotal = preçototal + valor_imposto


print(f"{pesokg} kilograma")
print(f"{preçototal} do transporte")
print(f"{valor_imposto} de imposto")
print(f"o valor total transportado é de {valortotal}")
