from abc import ABC, abstractmethod

from datetime import datetime


class File(ABC):
    def __init__(self, path):
        self.path = path

    @abstractmethod
    def read(self):
        pass
