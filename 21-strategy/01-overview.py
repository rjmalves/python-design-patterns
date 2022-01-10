# Muitos algoritmos podem ser decompostos em partes de alto
# e baixo níveis. Por exemplo, quando se vai descrever um
# algoritmo para fazer chá:

# Processo de alto nível (mais genérico)
#   - Processo de fazer uma bebida quente qualquer
#   - Aquecer água
#   - Colocar em uma xícara

# Processo de baixo nível (específico)
#   - Organizar as folhas de chá em um saco
#   - Mergulhar o saco na água para infusionar

# Desta forma, o processo de alto nível pode ser reutilizado
# em outras situações, como fazer café ou chocolate quente.
# Dizemos que o processo de alto nível é suportado por diferentes
# estatégias (strategies) de bebidas quentes.

# O padrão strategy habilita a escolha do comportamento exato
# de um módulo do sistema ser escolhido apenas em tempo
# de execução.
