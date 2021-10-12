# Alguns componentes do sistema so precisam ser instanciados
# uma unica vez. O padrao singleton e usado para esses casos.

# Por exemplo, repositorios de bancos de dados e factories de objetos
# nao precisam ser inicializados o tempo todo, ja que seu processo
# de inicializacao e custoso.

# Desta maneira, os objetos sao inicializados uma unica vez e todos
# os membros do codigo que o usam fazem uso da mesma instancia.

# Devemos prevenir a criacao de copias adicionais e cuidar do
# processo de lazy instantiation.
