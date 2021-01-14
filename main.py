from abc import ABC, abstractmethod


class A(ABC):

    @abstractmethod
    def a_method(self): pass


class Mix(ABC):

    @abstractmethod
    def my_mix(self): pass


class B(A, Mix):

    def a_method(self): pass

    def my_mix(self): pass


print(B.mro())



