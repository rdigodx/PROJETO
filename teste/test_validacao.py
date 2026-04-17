from sistema import validacao


def test_validar_nome_valido():
    assert validacao.validar_nome("Maria Silva") is True


def test_validar_nome_invalido():
    assert validacao.validar_nome("Maria123") is False


def test_validar_nota_valida():
    assert validacao.validar_nota(7.5, 8.0) is True


def test_validar_nota_invalida():
    assert validacao.validar_nota(11.0, 8.0) is False


def test_validar_data_valida(data_nascimento_para_idade):
    data_valida = data_nascimento_para_idade(14)
    resultado = validacao.validar_data_nascimento(data_valida)
    assert isinstance(resultado, int)


def test_validar_data_invalida():
    assert validacao.validar_data_nascimento("31/02/2012") is None


def test_validar_idade_valida(data_nascimento_para_idade):
    data_idade_valida = data_nascimento_para_idade(12)
    idade = validacao.validar_data_nascimento(data_idade_valida)
    assert idade is not None
    assert 12 <= idade <= 18


def test_validar_idade_invalida(data_nascimento_para_idade):
    data_idade_invalida = data_nascimento_para_idade(10)
    assert validacao.validar_data_nascimento(data_idade_invalida) is None
