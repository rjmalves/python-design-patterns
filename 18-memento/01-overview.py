# Um objeto em um sistema pode sofrer diversas modificações.
# Por exemplo, uma conta de banco é alterada com depósitos e saques.

# Podemos navegar nessas mudanças de diferentes maneiras.
# Uma delas é guardando cada mudança, por meio do Command Pattern,
# e implementar um 'undo' para cada comando

# Outra maneira é fazer um snapshot do sistema a cada instante (Memento).
# Um Memento é um token/handle representando um estado do sistema.
# Permite que voltemos para o estado em que o token foi gerado, expondo
# direta ou indiretamente a informação necessária.
