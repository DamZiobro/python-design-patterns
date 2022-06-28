#! /usr/bin/env python

import abc
from typing import List, Any, Optional

#============= PRODUCTS =======================================
class Building:
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self._parts: List[Any] = []

    def add(self, part: Any):
        self._parts.append(part)

    def describe(self):
        print(f"{self.__class__.__name__} parts: {', '.join(self._parts)}")

class Home(Building):
    pass


#============= BUILDERS =======================================

class Builder:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def reset(self):
        pass

    @abc.abstractmethod
    def produce_door(self):
        pass

    @abc.abstractmethod
    def produce_window(self):
        pass
        
    @abc.abstractmethod
    def produce_roof(self):
        pass

    @abc.abstractmethod
    def produce_walls(self):
        pass

    @abc.abstractmethod
    def produce_interiors(self):
        pass

class HomeBuilder(Builder):

    def __init__(self):
        self.reset()

    def reset(self):
        self._product: Home = Home()

    @property
    def product(self):
        return self._product

    def produce_door(self):
        self._product.add("Home door")

    def produce_window(self):
        self._product.add("Home window")
        
    def produce_roof(self):
        self._product.add("Home roof")

    def produce_walls(self):
        self._product.add("Home walls")

    def produce_interiors(self):
        self._product.add("Home interiors")

#============= DIRECTORS =======================================

class Director:

    def __init__(self, builder: Builder):
        self._builder: Builder = builder

    @abc.abstractmethod
    def build_raw_open_state(self):
        pass

    @abc.abstractmethod
    def build_raw_closed_state(self):
        pass

    @abc.abstractmethod
    def build_fully_featured_state(self):
        pass

class HomeDirector(Director):

    def build_raw_open_state(self):
        self._builder.reset()
        self._builder.produce_walls()
        self._builder.produce_roof()

    def build_raw_closed_state(self):
        self._builder.reset()
        self.build_raw_open_state()
        self._builder.produce_window()
        self._builder.produce_door()


    def build_fully_featured_state(self):
        self._builder.reset()
        self.build_raw_closed_state()
        self._builder.produce_interiors()

#============= MAIN =======================================

if __name__ == "__main__":    
    builder: Builder = HomeBuilder()
    director: Director = HomeDirector(builder)
    
    director.build_raw_open_state()
    builder.product.describe()

    director.build_raw_closed_state()
    builder.product.describe()

    director.build_fully_featured_state()
    builder.product.describe()
