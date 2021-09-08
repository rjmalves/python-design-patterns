# Essa seção irá tratar de dois padrões de design:
# - Factory Method
# - Abstract Factory

# Às vezes a lógica de inicialização de objetos fica
# muito complicada. O método de criação (__init__) não
# é muito descritivo:
#  - O nome é fixo
#  - Não pode ser sobrescrito para diferentes argumentos
#  - Pode acabar se tornando um abismo de parâmetros opcionais

# A criação de um objeto (completa, não por partes como no Builder)
# pode ser tercerizada:
#  - Um método exclusivo para criar o objeto (Factory Method)
#  - Uma classe exclusiva para criar objetos (Factory)
#  - Uma hierarquia de classes para criação (Abstract Factory)

# Uma factory é um componente responsável somente pela criação
# completa de objetos.
