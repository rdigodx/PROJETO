from sistema import organizacao


def test_listar_alunos(lista_alunos_exemplo_valor_none):
    listar = organizacao.listar_alunos(lista_alunos_exemplo_valor_none)
    assert listar == lista_alunos_exemplo_valor_none

def test_listar_alunos(lista_alunos_exemplo):
    listar = organizacao.listar_alunos(lista_alunos_exemplo)
    assert listar == lista_alunos_exemplo

def test_separar_alunos(lista_alunos_exemplo):
    aprovados, reprovados = organizacao.separar_alunos(lista_alunos_exemplo)

    assert len(aprovados) == 2
    assert len(reprovados) == 1
    assert all(aluno["status"] == "APROVADO" for aluno in aprovados)
    assert all(aluno["status"] == "REPROVADO" for aluno in reprovados)


