# O padrao Bridge e usado principalmente para evitar uma
# explosao de tamanho dos modelos, na forma de um produto
# cartesiano.

# Ele permite que se desacople a interface (hierarquia)
# da implementacao (outra hierarquia).

# Por exemplo, supondo que serao desenvolvidos gerenciadores
# de threads, que tem como classe base a ThreadScheduler.

# Gerenciadores de threads podem ser preemptivos ou cooperativos,
# o que nos da 2 possibilidades quanto ao modo de funcionamento
# (implementacao).

# Tambem podemos quere executar em ambientes de Windows ou Unix, o
# que nos da 2 possibilidades quanto ao modo de uso (interface).

# A rigor, seriam feitas 4 implementacoes: WindowsPTS, WindowsCTS,
# UnixPTS e UnixCTS.

# Na hierarquia:

#                          ThreadScheduler
#                                 |
#                -----------------------------------
#                |                                 |
#     PreempitveThreadScheduler         CooperativeThreadScheduler
#                |                                 |
#      ------------------------          -------------------------
#      |                      |          |                       |
#  WindowsPTS              UnixPTS   WindowsCTS               UnixCTS

# Ao se usar o padrao Bridge, podemos alterar a forma com que esses objetos
# se relacionam:

# PreemptiveThreadScheduler    CooperativeThreadScheduler
#           |                              |
#           --------------------------------
#                           |
#                   ThreadScheduler (IPlatformScheduler - interface)
#                           |
#           --------------------------------
#           |                              |
#    WindowsScheduler                UnixScheduler
