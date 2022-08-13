#! /usr/bin/env python

import abc
import time


class Observer:

    @abc.abstractmethod
    def update(self):
        pass


class FirstObserver(Observer):

    def update(self):
        print(f"updating old {self.__class__.__name__}...")


class SecondObserver(Observer):

    def update(self):
        print(f"updating new {self.__class__.__name__}...")


class Observable:

    def __init__(self):
        self._observers = set()

    def register(self, observer: Observer):
        self._observers.add(observer)

    def unregister(self, observer: Observer):
        self._observers.add(observer)

    def update(self):
        for observer in self._observers:
            observer.update()
        
        
if __name__ == "__main__":    
    observable = Observable()
    observable.register(FirstObserver())
    observable.register(SecondObserver())

    observable.update()
