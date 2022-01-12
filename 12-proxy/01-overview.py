
# Suponha que está sendo chamada uma função foo.Bar().
# Assume-se que foo está no mesmo processo que Bar(). Porém,
# é possível que, no futuro, seja necessário transportar todas as
# operações relacionadas a foo para um processo separado.
# Como é possível fazer isso sem alterar o código?

# O padrão Proxy é usado pra isso. Você pode manter a interface, tendo
# um comportamento implementado totalmente diferente. Esta é uma
# communication proxy, mas existem outras: logging, virtual, guarding, etc..

# A Proxy é uma classe que funciona como interface para um recurso específico.
# O recurso pode ser remoto, custoso, ou querer logging. A ideia é a mesma.
