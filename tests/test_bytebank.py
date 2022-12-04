import pytest
from pytest import mark

from src.bytebank import Funcionario

class TestClass:

  def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
    # Given
    entrada = '13/03/2000'
    esperado = 22

    funcionario_teste = Funcionario('Teste', entrada, 1111)

    # When
    resultado = funcionario_teste.idade

    # Then
    assert resultado == esperado
  
  def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
    funcionario_teste = Funcionario('Lucas Carvalho', '13/03/2022', 1111)

    resultado = funcionario_teste.sobrenome()

    assert resultado == 'Carvalho'

  def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
    funcionario_teste = Funcionario('Paulo Bragança', '11/11/2000',100000)

    resultado = funcionario_teste.decrescimo_salario()

    assert resultado == 90000

  @mark.calcular_bonus
  def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
    funcionario_teste = Funcionario('Teste', '11/11/2000', 1000)
    
    resultado = funcionario_teste.calacular_bonus()

    assert resultado == 100

  @mark.calcular_bonus
  def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
    with pytest.raises(Exception):
      funcionario_teste = Funcionario('Teste', '11/11/2000', 1000000)
    
      resultado = funcionario_teste.calacular_bonus()

      assert resultado
