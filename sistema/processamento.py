def cria_aluno(nome, data_nascimento, idade, nota1, nota2, media, status, lista_alunos):
        cadastro ={
                'aluno': nome,
                'data_nascimento': data_nascimento,
                'idade': idade,
                'n1': nota1,
                'n2': nota2,
                'media': media,
                'status': status
            }

        lista_alunos.append(cadastro)
        print(f"\nAluno '{nome}' cadastrado com sucesso!\n")


def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

def classificar_aluno(media):
    status = "APROVADO" if media >= 7 else "REPROVADO"
    return status

