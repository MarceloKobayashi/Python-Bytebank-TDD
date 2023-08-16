import pytest
from codigo.Funcionario_1 import Funcionario
from pytest import mark


class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        entrada = '13/03/2000'                          # Given(Contexto)
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade()           # When(Ação)

        assert resultado == esperado                    # Then(Desfecho)

    def test_quando_sobrenome_recebe_lucas_carvalho_deve_retornar_carvalho(self):
        entrada = ' Lucas Carvalho '                                                            # Given
        esperado = 'Carvalho'

        funcionario_teste = Funcionario(entrada, '29/11/2004', 1111)
        resultado = funcionario_teste.sobrenome()                                               # When

        assert resultado == esperado                                                            # Then

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado_salario = 90000                                                                        # Given

        funcionario_teste = Funcionario(entrada_nome, '29/11/2004', entrada_salario)
        funcionario_teste.decrescimo_salario()                                                          # When
        resultado = funcionario_teste.salario

        assert resultado == esperado_salario                                                            # Then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000                                                                                  # Given
        esperado = 100

        funcionario_teste = Funcionario('Teste', '29/11/2004', entrada)                                 # When
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado                                                                    # Then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 1000000                               # esperado já está nesse pytest.raises(Exception)

            funcionario_teste = Funcionario('Teste', '29/11/2004', entrada)
            resultado = funcionario_teste.calcular_bonus()

            assert resultado                                # compara o resultado com o esperado(pytest.raises)
