"""
Assert: Afirmem que a condição é verdadeira, confirme
pytest: Como se fosse uma biblioteca de testes. Bota pytest no terminal e ele roda todos os testes

"""
from calculadora import quadrado
def teste_posi():
    assert quadrado(2) == 4
    assert quadrado(3) == 9
    assert quadrado(4) == 16
def teste_neg():
    assert quadrado(-2) == 4
    assert quadrado(-3) == 9
    assert quadrado(-4) == 16

















































