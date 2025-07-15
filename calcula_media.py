
def verificar_aprovacao(notas):
    """
    Verifica o status de aprovação de um aluno com base na média de quatro notas.

    Regras de Negócio:
    1. A entrada deve ser uma lista contendo 4 números (inteiros ou reais).
    2. A média final é a soma das 4 notas dividida por 4.
    3. Se a média for > 7.0: 'Aprovado'
    4. Se a média for > 5.0 e <= 7.0: 'Recuperação'
    5. Se a média for <= 5.0: 'Reprovado'

    Args:
        notas (list): Uma lista contendo 4 notas numéricas.

    Returns:
        str: O status do aluno ('Aprovado', 'Recuperação', 'Reprovado')
             ou uma mensagem de erro caso a entrada seja inválida.
    """
    # 1. Verifica se a entrada é uma lista
    if not isinstance(notas, list):
        return "Erro: A entrada deve ser uma lista de notas."

    # 2. Verifica se a lista tem exatamente 4 notas
    if len(notas) != 4:
        return "Erro: A lista deve conter exatamente 4 notas."

    # 3. Verifica se todas as notas são números (int ou float)
    for nota in notas:
        if not isinstance(nota, (int, float)):
            return "Erro: A lista deve conter apenas números reais."

    # 4. Calcula a média
    media = sum(notas) / 4

    # 5. Avalia o status do aluno
    if media > 7.0:
        return 'Aprovado'
    elif media > 5.0 and media <= 7.0:
        return 'Recuperação'
    else:
        return 'Reprovado'