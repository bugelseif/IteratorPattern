# modulo que implementa o Iterator
from collections.abc import Iterator, Iterable


# criando iterador de ordem de inserção
class InsertOrder(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection: Iterable, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    # itera o objeto até não ter mais posições de indices,
    # caindo na except
    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return value

# criando um objeto iteravel
class WordsCollection(Iterable):
    def __init__(self, collection: list = []) -> None:
        self._collection = collection

    def __iter__(self) -> InsertOrder:
        return InsertOrder(self._collection)

    def get_reverse(self) -> InsertOrder:
        return InsertOrder(self._collection, True)
    
    def outras_formas(self) -> InsertOrder:
        # desenvolver outras formas de percorrer a coleção
        ...

    def add_item(self, item):
        self._collection.append(item)