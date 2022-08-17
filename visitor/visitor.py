#! /usr/bin/env python

import enum
from abc import ABCMeta, abstractmethod
from typing import List


class HomeElement:

    def accept(self, visitor):
        visitor.visit(self)


class HomeVisitor(metaclass=ABCMeta):

    def __init__(self, home_elements: List[HomeElement]):
        self._home_elements = home_elements

    def visit(self):
        print(f"visiting by: {self.__class__.__name__}")
        for home_element in self._home_elements:
            home_element.accept(self)

    @abstractmethod
    def visit_light(self):
        pass

    @abstractmethod
    def visit_thermostat(self):
        pass


class LightStatus(enum.Enum):
    enabled = "enabled"
    disabled = "disabled"


class ThermostatStatus(enum.Enum):
    enabled = "enabled"
    disabled = "disabled"


class Light(HomeElement):

    def __init__(self):
        self.status: LightStatus = LightStatus.disabled

    def set_status(self, status: LightStatus):
        print(f"setting status to {status}")
        self.status = status

    def accept(self, visitor: HomeVisitor):
        visitor.visit_light(self)


class Thermostat(HomeElement):

    def __init__(self):
        self.status: ThermostatStatus = ThermostatStatus.disabled

    def set_status(self, status: ThermostatStatus):
        print(f"setting status to {status}")
        self.status = status

    def accept(self, visitor: HomeVisitor):
        visitor.visit_thermostat(self)


class HomeOwnerVisitor(HomeVisitor):

    def visit_light(self, light: Light):
        light.set_status(LightStatus.enabled)

    def visit_thermostat(self, thermostat: Thermostat):
        light.set_status(ThermostatStatus.enabled)


class NonOwnerVisitor(HomeVisitor):

    def visit_light(self, light: Light):
        light.set_status(LightStatus.disabled)

    def visit_thermostat(self, thermostat: Thermostat):
        light.set_status(ThermostatStatus.disabled)

if __name__ == "__main__":    

    light = Light()
    thermostat = Thermostat()

    owner_visitor = HomeOwnerVisitor([light, thermostat])
    owner_visitor.visit() 

    non_owner_visitor = NonOwnerVisitor([light, thermostat])
    non_owner_visitor.visit() 
