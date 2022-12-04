from datetime import date

class Funcionario:
  def __init__(self, nome, data_nascimento, salario) -> None:
    self._nome = nome
    self._data_nascimento = data_nascimento
    self._salario = salario

  @property
  def nome(self):
    return self._nome
  
  @property
  def salario(self):
    return self._salario
  
  @property
  def idade(self):
    return date.today().year - int(self._data_nascimento.split('/')[-1])

  def sobrenome(self):
    nome_completo = self._nome.strip()
    return nome_completo.split(' ')[-1]

  def decrescimo_salario(self):
    if self._salario >= 100000 and self._eh_socio():
      return self._salario * 0.9
  
  def _eh_socio(self):
    sobrenomes = ['Bragança', 'Windor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
    return self.sobrenome() in sobrenomes

  def calacular_bonus(self):
    valor = self._salario * 0.1
    if valor > 1000:
      raise Exception('O salário é muito alto para receber um bônus')
    return valor
  
  def __str__(self) -> str:
    return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'
  
