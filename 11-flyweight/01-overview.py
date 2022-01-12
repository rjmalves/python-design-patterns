
# A principal finalidade do Flyweight é economizar
# espaço de armazenamento de dados.

# Por exemplo, em um MMORPG, onde existem muitos usuários
# com nomes e/ou sobrenomes repetidos.
# Não faz sentido armazenar tantos nomes repetidos em um banco
# de dados.
# É melhor salvar um índice de nomes e relacionar apenas um conjunto
# de índices a cada jogador, ao invés das strings completas.

# Outro exemplo é formatação de texto.
# Não queremos que cada caractere tenha campos para dizer qual o formato
# que deve ser usado na renderização (fonte, negrito, itálico, etc.).
# Podemos operar em ranges (por ex. negrito começa na linha x coluna y e
# vai até a linha z coluna w).

# Flyweight se trata de armazenar os dados externamente e referenciar
# nos objetos em questão.
