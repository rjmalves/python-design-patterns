
# Ações normais em programação não são reversíveis.
# Por exemplo, não é possível desfazer uma atribuição
# sem uma lógica específica para isso, ou serializar uma
# sequência de chamadas que foram realizadas.

# Desejamos um objeto para representar uma operação, como por exemplo:
#   - Um objeto Person deve alterar seu campo Age para 22
#   - Um objeto Car deve chamar o método explode()

# Podem ser usados em contextos:
#   - Comandos de GUI
#   - Recurso de undo/redo multinível
#   - Gravação de macros
