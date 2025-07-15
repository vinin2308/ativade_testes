from calcula_media import verificar_aprovacao

def test_aprovado_particao_equivalencia():
    assert verificar_aprovacao([8.0, 9.0, 7.5, 9.5]) == 'Aprovado'

def test_recuperacao_particao_equivalencia():
    assert verificar_aprovacao([6.0, 5.5, 5.5, 6.0]) == 'Recuperação'

def test_reprovado_particao_equivalencia():
    assert verificar_aprovacao([4.0, 5.0, 4.5, 5.0]) == 'Reprovado'

def test_recuperacao_limite_valor_limite():
    assert verificar_aprovacao( [7.0, 7.0, 7.0, 7.0]) == 'Recuperação'

def test_aprovado_limite_valor_limite():
    assert verificar_aprovacao( [7.1, 7.1, 7.1, 7.1]) == 'Aprovado'

def test_reprovado_limite_valor_limite():
    assert verificar_aprovacao( [5.0, 5.0, 5.0, 5.0]) == 'Reprovado'

def test_recupracao_minimo_valor_limite():
    assert verificar_aprovacao( [5.1, 5.1, 5.1, 5.1]) == 'Recuperação'

def test_nota_maxima_particao_equivalencia():
    assert verificar_aprovacao([10, 10, 10, 10] ) == 'Aprovado'

def test_3entradas_validacao_entrada():
    assert verificar_aprovacao([7.0, 8.0, 6.0]) == 'Erro: A lista deve conter exatamente 4 notas.'

def test_entrada_inteira_validacao_entrada():
    assert verificar_aprovacao([7.0, 8.0, 6.0, '9']) == 'Erro: A lista deve conter apenas números reais.'
