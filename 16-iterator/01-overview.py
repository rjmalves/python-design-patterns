# Iterar ou atravessar é uma funcionalidade fundamental
# de várias estruturas de dados.

# Um Iterator é uma classe que facilita esta travessia:
#   - Mantendo uma referência para o elemento atual
#   - Sabendo navegar para o próximo elemento

# O protocolo de Iterator necessita de:
#   - __iter__() para expor o iterator, que usa
#   - __next__() para retornar cada um dos elementos iterados ou
#   - raise StopIteration quando acabar.

