#! /usr/bin/env python


class Strategy:
    pass


class FirstStrategy(Strategy):
    def execute(self):
        print("executying FirstStrategy")


class SecondStrategy(Strategy):
    def execute(self):
        print("executying SecondStrategy")


class Executor:
    def __init__(self, strategy):
        self.set_strategy(strategy)

    def set_strategy(self, strategy: Strategy):
        self._strategy: Strategy = strategy

    def execute(self):
        return self._strategy.execute()
        

if __name__ == "__main__":    
    executor = Executor(FirstStrategy())
    executor.execute()
    executor.set_strategy(SecondStrategy())
    executor.execute()

    
