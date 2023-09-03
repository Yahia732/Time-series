from File_Manager.File import File


class configuration_manager:
    def __init__(self,reader:File):
        self.reader=reader
    def read(self):
        """
        Reads the model parameters from a file
        """
        return self.reader.read()