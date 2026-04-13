
def media_da_turma(lista_alunos):
    soma_das_medias = 0
    
    for cadastro in lista_alunos:
        media_aluno = sum(cadastro['notas']) / len(cadastro['notas'])
        soma_das_medias += media_aluno

    return soma_das_medias / len(lista_alunos)

def melhor_aluno(lista_alunos):
    for notas in enumerate(lista_alunos):
        media = sum(notas) / len(notas)
        
        if media > melhor_media:
            melhor_media = media
    
    return melhor_media