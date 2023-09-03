from File_Manager.File import File
import yaml
from datetime import datetime
class yaml_file(File):
    def read(self):
        """
        Reads a yaml file

        """
        with open(self.path, "r") as stream:
            try:
                file= yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print("File not found")
        return self.file
