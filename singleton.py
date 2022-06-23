#! /usr/bin/env python


class Singleton(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(Singleton, cls).__new__(cls)
            # Put any initialization here.
        return cls._instance


if __name__ == "__main__":    
    singleton1 = Singleton()
    singleton2 = Singleton()

    print(f"singleton1: {singleton1}")
    print(f"singleton2: {singleton2}")
    print('Are they the same object?', singleton1 is singleton2)
