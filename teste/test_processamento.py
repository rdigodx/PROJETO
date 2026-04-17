from sistema import processamento


def test_calcular_media():
    assert processamento.calcular_media(8.0, 6.0) == 7.0


def test_classificar_aprovado():
    assert processamento.classificar_aluno(7.0) == "APROVADO"


def test_classificar_reprovado():
    assert processamento.classificar_aluno(6.9) == "REPROVADO"


def test_criar_aluno():
    lista_alunos = []

    processamento.cria_aluno(
        nome="LUCAS",
        data_nascimento="10/08/2010",
        idade=15,
        nota1=7.0,
        nota2=8.0,
        media=7.5,
        status="APROVADO",
        lista_alunos=lista_alunos,
    )

    assert len(lista_alunos) == 1
    assert lista_alunos[0]["aluno"] == "LUCAS"
    assert lista_alunos[0]["media"] == 7.5
    assert lista_alunos[0]["status"] == "APROVADO"
