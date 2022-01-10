# Do Strategy Pattern, sabemos que algoritmos podem ser quebrados
# em partes.

# O Strategy faz isso através de composição. Isto é, um algoritmo
# "de alto nível" espera estratégias que atendam certas interfaces.
# Implementações concretas precisam atender às interfaces.

# Template Method faz isso através de herança.
# O algoritmo completo é definido na classe base, fazendo uso
# de membros abstratos.
# Herdeiros da classe base sobrescrevem os membros abstratos
# e o "método template" é chamado para resolver o problema.

# Template Method permite dsenhar o esqueleto de um algoritmo
# concreto sem dizer os detalhes, que são especificados
# nas subclasses.
