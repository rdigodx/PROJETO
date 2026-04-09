
def media_da_turma(lista_alunos):
    for notas in lista_alunos:
        calculo_media = sum(notas) / len(notas)
    return calculo_media


def melhor_aluno(lista_alunos):
    for notas in enumerate(lista_alunos):
        media = sum(notas) / len(notas)
        
        if media > melhor_media:
            melhor_media = media
    
    return melhor_media