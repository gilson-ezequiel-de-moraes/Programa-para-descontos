valor_total = float(input("Digite o valor total da compra (R$): "))

# Determina a porcentagem de desconto com base nas regras estipuladas
if valor_total < 200.00:
    percentual_desconto = 0.05  # 5%
elif valor_total < 300.00:
    percentual_desconto = 0.10  # 10%
else:
    percentual_desconto = 0.15  # 15%

# Calcula o valor do desconto e o valor final a ser pago
valor_desconto = valor_total * percentual_desconto
valor_final = valor_total - valor_desconto

# Exibe os resultados formatados
print("-" * 35)
print(f"Valor total da compra: R$ {valor_total:.2f}")
print(f"Desconto aplicado ({int(percentual_desconto * 100)}%): R$ {valor_desconto:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")
print("-" * 35)
