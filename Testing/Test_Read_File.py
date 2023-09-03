import unittest

from File_Manager.json_file import json_file
from File_Manager.yaml_file import yaml_file


class Test_Read_File(unittest.TestCase):
    def setup(self) -> None:
        self.file1=json_file("C:/Users/yahia.sedki/PycharmProjects/timeseriesgenerator/Time Series.json")
        self.file2=yaml_file("C:/Users/yahia.sedki/PycharmProjects/timeseriesgenerator/Time Series.yaml")
    def test_json_file(self):
        self.setup()
        start_date,end_date,variables=self.file1.read()
        self.assertEquals(variables["Sampling Frequency in Minutes"],"1D")
    def test_yaml_file(self):
        self.setup()
        start_date,end_date,variables=self.file2.read()
        self.assertEquals(variables["Time-Series Data Type"],"multiplicative")
