
# Às vezes precisamos definir uma nova operação em toda
# uma hierarquia de clases. Por exemplo, tornam um modelo
# de documento exportável para HTML/Markdown.

# O modelo de documento pode conter vários elementos, que
# inclusive podem conter outros elementos.
# Não queremos entrar em cada classe dessa hierarquia e modificá-la,
# adicionando outras funcionalidades;

# Podemos criar um componente externo que gerencia a renderização
# Tentaremos ao máximo evitar verificações explícitas de tipo

# O Visitor é um componente que sabe percorrer uma estrutura
# de dados composta de tipo (possivelmente) relacionados.
