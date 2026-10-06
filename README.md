# Sistema de Gerenciamento Escolar

## 1. Classes

### Escola

**Atributos:**
- nome
- salas
- professores

**Métodos:**
- adicionar_sala()
- adicionar_professor()
- mostrar_informações()

### SaladeAula

**Atributos:**
- numero
- capacidade

**Métodos:**
- mostrar_informações()

### Professor

**Atributos:**
- nome
- disciplina

**Métodos:**
- mostrar_informações()

### Aluno

**Atributos:**
- nome
- idade
- matrícula

**Métodos:**
- adicionar_endereço
- mostrar_informações

### Endereço

**Atributos:**
- rua
- numero
- cidade
- estado

**Métodos:**
- mostrar_informações()

## 2. Relacionamentos

### Escola ——◆ SalaDeAula

Tipo: Composição (◆)

Uma escola possui várias salas de aula. As salas dependem da escola para existir no sistema. Se a escola for removida, suas salas também deixam de existir.

### Escola ——— Professor

Tipo: Associação

Um professor pode lecionar em várias escolas e uma escola pode possuir vários professores. Ambos podem existir independentemente.

### Aluno ——◇ Endereço

Tipo: Agregação (◇)

O aluno possui um endereço, mas o endereço pode continuar
existindo mesmo que o aluno seja removido.