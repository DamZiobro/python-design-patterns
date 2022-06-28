#! /usr/bin/env python

import copy 
from abc import ABCMeta, abstractmethod

class Prototype(metaclass=ABCMeta):
    @abstractmethod
    def clone(self):
        pass


class Concrete(Prototype):
    def clone(self):
        return copy.deepcopy(self)
        

if __name__ == "__main__":    
    object1 = Concrete()
    object2 = object1
    object3 = object1.clone()

    print("object1 is object2: ", object1 is object2)
    print("object1 is object3: ", object1 is object3)
    
