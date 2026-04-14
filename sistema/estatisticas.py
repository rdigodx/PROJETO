def media_da_turma(lista_alunos):
    soma_das_medias = 0
    for cadastro in lista_alunos:
        notas = cadastro.get('notas')
        if notas: 
            media_aluno = sum(notas) / len(notas)
            soma_das_medias += media_aluno
            
    return soma_das_medias / len(lista_alunos) if lista_alunos else 0

def melhor_aluno(lista_alunos):
    melhor_media = 0 
    
    for cadastro in lista_alunos:
        
        media = sum(cadastro['notas']) / len(cadastro['notas'])
        
        if media > melhor_media:
            melhor_media = media
            
    return melhor_media
