# Esercizio 7 alt.
import unittest
from Esercizio6 import CSVFile

class TestCSVFile(unittest.TestCase):
    def test_init(test):
        csv_file = CSVFile("test_data.csv")
        self.assertEqual(csv_file.name, "test_data.csv")