
# Em determinados momentos precisamos de incrementar um
# objeto com mais funcionalidades e não desejamos reescrever
# código ou alterar código existente (OCP)

# Também não queremos adicionar mais de uma responsabilidade
# em um mesmo objeto (SRP). Logo, devemos conseguir
# interagir com as estruturas já existentes.

# Nestas situações temos duas opções:
#   - Herdar do objeto (se possível)
#   - Fazer um Decorator, que simplesmente faz uma referência
#   - para o objeto decorado e adiciona a funcionalidade

# Desta forma, usamos o decorator APENAS quando não é possível
# de se fazer a modificação desejada por herança.
