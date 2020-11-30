class Pessoa:
    def __init__(self, codigo, nome, endereco, telefone):
        self.__codigo = codigo
        self.nome = nome
        self._endereco = endereco
        self.__telefone = telefone

    def __imprimeTelefone(self):
        print(self.__telefone)


    def imprimeNome(self):
        print(self.nome)


class Fisica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone, cpf, idade, peso, altura):
        Pessoa.__init__(self, codigo, nome, endereco, telefone)
        self.__cpf = cpf
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def imprimeCPF(self):
        print(self.__cpf)

    def __calculaIMC(self, resultado):
        self.resultado = self.peso / self.altura
        return resultado

class Juridica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone, cnpj, inscricaoEstadual, quantidadeFuncionarios):
        Pessoa.__init__(self, codigo, nome, endereco, telefone)
        self.__cnpj = cnpj
        self.__inscricaoEstadual = inscricaoEstadual
        self.quantidadeFuncionarios = quantidadeFuncionarios

    def imprimeCNPJ(self):
        print(self.__cnpj)

    def __emitirNotaFiscal(self):
        print("CNPJ: ", self.__cnpj, "Inscrição Estadual: ", "Quantidade de funcionários: ", self.quantidadeFuncionarios)