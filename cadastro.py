class Funcionario:
    def __init__(self, nome, email, cor, rg, idade, salario):
        self.nome = nome
        self.email = email
        self.cor = cor
        self.rg = rg
        self.idade = idade
        self.salario = salario

    def __str__(self):
        return f"Olá {self.nome}, você foi cadastrado com sucesso em nosso sistema"
    def aumentar_salario(self, aumento):
        return self.salario + aumento


esse_funcionario = Funcionario(
    nome = 'Andre',
    email = 'almeida.andre83@gmail.com',
    cor = 'parda',
    rg = 4348234,
    idade = 27,
    salario = 2000
)



print(esse_funcionario)
print(esse_funcionario.aumentar_salario(50))
