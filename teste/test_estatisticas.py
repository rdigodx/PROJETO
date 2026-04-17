from sistema import estatisticas


def test_calcular_media_da_turma(lista_alunos_exemplo):
    media = estatisticas.media_da_turma(lista_alunos_exemplo)
    assert media == (8.5 + 5.5 + 9.0) / 3


def test_obter_melhor_aluno(lista_alunos_exemplo):
    nome, media = estatisticas.melhor_aluno(lista_alunos_exemplo)
    assert nome == "CARLA"
    assert media == 9.0
