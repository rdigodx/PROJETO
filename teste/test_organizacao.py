from sistema import organizacao

def test_separar_alunos(lista_alunos_exemplo):
    aprovados, reprovados = organizacao.separar_alunos(lista_alunos_exemplo)

    assert len(aprovados) == 2
    assert len(reprovados) == 1
    assert all(aluno["status"] == "APROVADO" for aluno in aprovados)
    assert all(aluno["status"] == "REPROVADO" for aluno in reprovados)


