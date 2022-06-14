"""1- Atribuição para lista de valores"""

x, y = 10, 20

a, b, c = 1, 2, 3

def pesoAltura():
    return 57, 1.70

peso, altura = exibe() # Cria as variáveis e atribui os valores do return a elas.

"""2- Atribuição aumentada """

x += 5 #Ao invés de fazer x = x + 5

"""3- Valores padrões de parâmetros """

def pagamento(val_horas, horas = 40):
    return val_horas * horas


"""4 - Assert"""


def pagamento(val_horas, horas = 40):
    assert val_horas >= 0 and horas > 0  # Define uma declaração de True.
    return val_horas * horas

