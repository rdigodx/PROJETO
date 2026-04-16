def media_da_turma(lista_alunos):
    if not lista_alunos:
        return 0

    soma_das_medias = 0
    for cadastro in lista_alunos:
        soma_das_medias += cadastro['media']

    return soma_das_medias / len(lista_alunos)


def melhor_aluno(lista_alunos):
    if not lista_alunos:
        return None, 0

    melhor = max(lista_alunos, key=lambda cadastro: cadastro['media'])
    return melhor['aluno'], melhor['media']
