#! /usr/bin/env python

from typing import Any

class Adaptee():

    def do_something_legacy(self, param1: Any, param2: Any, param3: Any):
        print(f"do_something: params {param1}, {param2}, {param3}")


class Adapter():

    def __init__(self, adaptee: Adaptee):
        self._adaptee = adaptee

    def do_required(self, param1: Any, param2: Any):
        self._adaptee.do_something_legacy(param1, param2, "FIXED_PARAM")


if __name__ == "__main__":    
    adaptee: Adaptee = Adaptee()
    adapter: Adapter = Adapter(adaptee)

    adapter.do_required(param1="PARAM1", param2="PARAM2")

