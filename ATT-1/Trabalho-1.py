# Sistema de gerenciamento escolar
# Atividade de Programação Orientada a Objetos

class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.salas = []
        self.professores = []

    def adicionar_sala(self, sala):
        self.salas.append(sala)

    def adicionar_professor(self, professor):
        self.professores.append(professor)

    def mostrar_informações(self):
        print(f"Escola: {self.nome}")
        print("Salas de aula:")
        for sala in self.salas:
            sala.mostrar_informações()
        print("Professores:")
        for professor in self.professores:
            professor.mostrar_informações()

class SalaDeAula:
    def __init__(self, numero, capacidade):
        self.numero = numero
        self.capacidade = capacidade

    def mostrar_informações(self):
        print(f"Sala de aula {self.numero} - Capacidade: {self.capacidade} alunos")

class Professor:
    def __init__(self, nome, disciplina):
        self.nome = nome
        self.disciplina = disciplina

    def mostrar_informações(self):
        print(f"O professor {self.nome} está ensinando {self.disciplina}")

class Aluno:
    def __init__(self, nome, idade, matrícula):
        self.nome = nome
        self.idade = idade
        self.matrícula = matrícula

    def adicionar_endereço(self, endereço):
        self.endereço = endereço

    def mostrar_informações(self):
        print(f"Aluno: {self.nome}, Idade: {self.idade}, Matrícula: {self.matrícula}")
        if  hasattr(self, 'endereço'):
            print(f"Endereço: {self.endereço.rua}, {self.endereço.numero}, {self.endereço.cidade} - {self.endereço.estado}")

class Endereço:
    def __init__(self, rua, numero, cidade, estado):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
        self.estado = estado

    def mostrar_informações(self):
        print(f"Endereço: {self.rua}, {self.numero}, {self.cidade} - {self.estado}")


escola = Escola("CEEP")

sala1 = SalaDeAula(1, 40)
sala2 = SalaDeAula(2, 40)
escola.adicionar_sala(sala1)
escola.adicionar_sala(sala2)

professor1 = Professor("Lucas", "Matemática")
escola.adicionar_professor(professor1)

aluno1 = Aluno("João", 15, "308")
endereço1 = Endereço("Rua A", 878, "Parnaíba", "PI")
aluno1.adicionar_endereço(endereço1)

escola.mostrar_informações()
aluno1.mostrar_informações()
