#! /usr/bin/env python

from abc import ABCMeta, abstractmethod

class AbstractTemplate(metaclass=ABCMeta):
    
    def execute(self):
        print("before step1...")
        self._step1()
        print("before step2...")
        self._step2()
        print("finish...")

    @abstractmethod
    def _step1(self):
        pass

    @abstractmethod
    def _step2(self):
        pass


class ConcreteExecute1(AbstractTemplate):

    def _step1(self):
        print("ConcreteExecute1._step1()")

    def _step2(self):
        print("ConcreteExecute1._step2()")

class ConcreteExecute2(AbstractTemplate):

    def _step1(self):
        print("ConcreteExecute2._step1()")

    def _step2(self):
        print("ConcreteExecute2._step2()")



if __name__ == "__main__":    
    ConcreteExecute1().execute()
    ConcreteExecute2().execute()
