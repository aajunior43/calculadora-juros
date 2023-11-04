# Definição da função para calcular juros simples
def calcular_juros_simples(principal, taxa, tempo):
    # Calcula os juros simples usando a fórmula J = P * T * R
    juros = principal * taxa * tempo
    # Retorna o valor dos juros
    return juros

# Definição da função para calcular juros compostos
def calcular_juros_compostos(principal, taxa, tempo):
    # Calcula os juros compostos usando a fórmula A = P * (1 + R) ** T
    montante = principal * ((1 + taxa) ** tempo)
    # Juros compostos são o montante menos o principal
    juros = montante - principal
    # Retorna o valor dos juros
    return juros

# Teste das funções com valores exemplo (pode remover esta parte ao integrar com a interface web)
if __name__ == "__main__":
    # Exemplo de uso para juros simples
    juros_simples = calcular_juros_simples(1000, 0.05, 2)
    print(f"Juros Simples: {juros_simples}")

    # Exemplo de uso para juros compostos
    juros_compostos = calcular_juros_compostos(1000, 0.05, 2)
    print(f"Juros Compostos: {juros_compostos}")
