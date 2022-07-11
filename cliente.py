# coleção criada emn interator.py
from iterator import WordsCollection

def instance_collection(elements: list[str]) -> WordsCollection:
    # instanciar coleção
    collection = WordsCollection()
    # popular lista
    for element in elements:
        collection.add_item(element)

    return collection

if __name__ == '__main__':
    # definição dos elementos
    elements = [
        'IFSC',
        'Programação',
        'Laboratório',
        'Professor',
        'Aluno'
        ]

    collection = instance_collection(elements)
    # apresenta elementos na ordem de inserção
    for e in collection.__iter__():
        print(e)
    # apresente elementos na ordem inversa
    for e in collection.get_reverse():
        print(e)