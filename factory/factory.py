#! /usr/bin/env python

import abc

class Shape():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print("drawing circle")


class Square(Shape):
    def draw(self):
        print("drawing square")


class AbstractFactory():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def make_object(self):
        return


class CircleFactory(AbstractFactory):
    def make_object(self):
        return Circle()
    

class SquareFactory(AbstractFactory):
    def make_object(self):
        return Square()


def draw_function(factory):
    drawable = factory.make_object()
    drawable.draw()


if __name__ == "__main__":    
    square_factory = SquareFactory()
    draw_function(square_factory)
    circle_factory = CircleFactory()
    draw_function(circle_factory)
