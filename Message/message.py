from abc import ABC, abstractmethod

class Message(ABC):
    @abstractmethod
    def __str__(self):
        pass
