#! /usr/bin/env python


class Singleton(object):
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
            # Put any initialization here.
        return cls._instance


if __name__ == "__main__":    
    singleton1 = Singleton.instance()
    singleton2 = Singleton.instance()

    print(f"singleton1: {singleton1}")
    print(f"singleton2: {singleton2}")
    print('Are they the same object?', singleton1 is singleton2)
