# A implementação de Proxy pode lembrar bastante
# as implementações clássicas de Decorator.

# Todavia, existem algumas diferenças:
#   - Proxy tem como objetivo prover uma interface idêntica
#   enquanto o Decorator fornece uma interface incrementada.
#   - Decorator tem uma referência para o objeto que está
#   decorando, enquanto Proxy não precisa.
#   - Proxy pode fazer referência a um objeto que ainda nem
#   existe, e só será criado quando necessário (Lazy);
