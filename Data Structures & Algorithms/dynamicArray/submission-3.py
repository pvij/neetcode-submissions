class DynamicArray:
    
    def __init__(self, capacity: int):
        self._arr = []
        self._capacity = capacity

    def get(self, i: int) -> int:
        return self._arr[i]

    def set(self, i: int, n: int) -> None:
        self._arr[i] = n

    def pushback(self, n: int) -> None:
        if len(self._arr) == self._capacity:
            self.resize()
        self._arr.append(n)

    def popback(self) -> int:
        last_elt = self._arr[-1]
        self._arr = self._arr[:-1]
        return last_elt

    def resize(self) -> None:
        self._capacity *= 2

    def getSize(self) -> int:
        return len(self._arr)
    
    def getCapacity(self) -> int:
        return self._capacity