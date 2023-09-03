from File_Manager.File import File
import json


class json_file(File):
    def read(self):
        """
        Reads a JSON file

        """
        with open(self.path, "r") as stream:
            file = json.loads(stream.read())
        return file
