#! /usr/bin/env python

from abc import abstractmethod


class Receiver():
    def print_message(self, text: str):
        print(f"Receiver received: {text}")


class Command():
    def __init__(self, receiver: Receiver, text: str):
        self._receiver = receiver
        self._text = text

    def execute(self):
        self._receiver.print_message(self._text)


class Invoker():
    def __init__(self):
        self._commands = []

    def add_command(self, command: Command):
        self._commands.append(command)

    def run(self):
        for command in self._commands:
            command.execute()


if __name__ == "__main__":    
    receiver: Receiver = Receiver()
    command1 = Command(receiver, "command text 1")
    command2 = Command(receiver, "command text 2")

    invoker = Invoker()
    invoker.add_command(command1)
    invoker.add_command(command2)

    invoker.run()

    
