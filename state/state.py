#! /usr/bin/env python


class StateMachine:
    def __init__(self):
        self.state1: State = ConcreteState1(self)
        self.state2: State = ConcreteState2(self)
        self.state: State  = self.state1

    def get_state(self):
        return self.state

    def switch(self):
        self.state.switch_state()


class State:
    def __init__(self, state_machine: StateMachine):
        self._state_machine: StateMachine = state_machine


class ConcreteState1(State):
    def switch_state(self):
        self._state_machine.state = self._state_machine.state2


class ConcreteState2(State):
    def switch_state(self):
        self._state_machine.state = self._state_machine.state1
        


if __name__ == "__main__":    
    state_machine = StateMachine()
    print(state_machine.get_state())
    state_machine.switch()
    print(state_machine.get_state())
    state_machine.switch()
    print(state_machine.get_state())
    
