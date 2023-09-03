from abc import ABC, abstractmethod


class file_save(ABC):
    def __init__(self, file_name, data):
        self.file_name = file_name
        self.data = data

    @abstractmethod
    def save(self):
        pass
