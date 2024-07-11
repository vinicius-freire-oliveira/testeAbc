# Importando a classe MutableSequence da biblioteca collections.abc
from collections.abc import MutableSequence

# Definindo a classe MinhaListinhaMutavel que herda de MutableSequence
class MinhaListinhaMutavel(MutableSequence):
    # Método inicializador que cria uma lista vazia para armazenar os dados
    def __init__(self):
        self._data = []

    # Método para obter um item da lista pelo índice
    def __getitem__(self, index):
        return self._data[index]

    # Método para definir um item na lista pelo índice
    def __setitem__(self, index, value):
        self._data[index] = value

    # Método para deletar um item da lista pelo índice
    def __delitem__(self, index):
        del self._data[index]

    # Método para retornar o comprimento da lista
    def __len__(self):
        return len(self._data)

    # Método para inserir um item na lista em um índice específico
    def insert(self, index, value):
        self._data.insert(index, value)

    # Método para representar a lista como uma string (útil para impressão)
    def __repr__(self):
        return repr(self._data)

# Criando e validando um objeto da classe MinhaListinhaMutavel
objetoValidado = MinhaListinhaMutavel()
print(objetoValidado)  # Deve imprimir: []

# Testando algumas operações
# Adicionando o valor 1 à lista
objetoValidado.append(1)
# Adicionando o valor 2 à lista
objetoValidado.append(2)
# Adicionando o valor 3 à lista
objetoValidado.append(3)
print(objetoValidado)  # Deve imprimir: [1, 2, 3]

# Modificando o valor no índice 1 para 4
objetoValidado[1] = 4
print(objetoValidado)  # Deve imprimir: [1, 4, 3]

# Deletando o valor no índice 2
del objetoValidado[2]
print(objetoValidado)  # Deve imprimir: [1, 4]

# Inserindo o valor 5 no índice 1
objetoValidado.insert(1, 5)
print(objetoValidado)  # Deve imprimir: [1, 5, 4]

# Imprimindo o comprimento da lista
print(len(objetoValidado))  # Deve imprimir: 3
