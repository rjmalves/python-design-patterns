
# Em algumas situações, em sistemas com múltiplos componentes,
# pode acontecer de alguns destes entrarem e outros saírem
#   - Salas de chat
#   - MMORPG

# Não faz sentido cada componente ter referências diretas para
# todos os outros, pois elas podem se tornar inválidas.

# Podemos fazer todos os componentes se comunicarem com um
# componente central, que facilita a comunicação.

# O padrão Mediator facilia a comunicação entre múltiplos componentes,
# uma vez que eles não precisam estar cientes de todos os outros
# que existem.
