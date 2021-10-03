class Cuboid:
 
    class ProducingAPI1:
 
        def produceCuboid(self, length, breadth, height):
 
            print(f'API1 is producing Cuboid with length = {length}, '
                  f' Breadth = {breadth} and Height = {height}')
 
    class ProducingAPI2:
        
        def produceCuboid(self, length, breadth, height):
            print(f'API2 is producing Cuboid with length = {length}, '
                  f' Breadth = {breadth} and Height = {height}')
 
 
    def __init__(self, length, breadth, height):
        self._length = length
        self._breadth = breadth
        self._height = height
 
    def produceWithAPI1(self): 
        objectAPIone = self.ProducingAPI1()
        objectAPIone.produceCuboid(self._length, self._breadth, self._height)
 
    def producewithAPI2(self):
        objectAPItwo = self.ProducingAPI2()
        objectAPItwo.produceCuboid(self._length, self._breadth, self._height)
 
    def expand(self, times):
        self._length = self._length * times
        self._breadth = self._breadth * times
        self._height = self._height * times
cuboid1 = Cuboid(1, 2, 3)
cuboid1.produceWithAPI1()
cuboid2 = Cuboid(19, 20, 21)
cuboid2.producewithAPI2()
