import unittest
import sys
sys.path.insert(0, r".\src")
from src.StrategyParserXML.Strategy import TreeStrategy, DomStrategy, SetParser
import unittest
import os
import xml.etree.ElementTree as ET

class TestParsingStrategies(unittest.TestCase):

    def setUp(self):
        
        self.xml_input_path = "./src/StrategyParserXML/xml_files/generated_sample.xml"
        self.datetime_tag = "MeseAnno"
        self.input_filter = "IT001E42718972222=13/2023"
        self.filtered_output_path = 'filtered.xml'

    def tearDown(self):
        
        if os.path.exists(self.filtered_output_path):
            os.remove(self.filtered_output_path)

    def test_tree_strategy(self):
        # Test per TreeStrategy
        tree_strategy = TreeStrategy()
        parser = SetParser(tree_strategy)
        parser.parse_xml(self.xml_input_path, self.datetime_tag, self.input_filter)

        # Verifica se il file filtrato contiene solo gli elementi attesi
        self.assertTrue(self.verify_filtered_file())

    def test_dom_strategy(self):
       
        dom_strategy = DomStrategy()
        parser = SetParser(dom_strategy)
        parser.parse_xml(self.xml_input_path, self.datetime_tag, self.input_filter)

 
        self.assertTrue(self.verify_filtered_file())

    def verify_filtered_file(self):
        # Legge il file filtrato e verifica se contiene solo gli elementi attesi
        expected_elements = ["IT001E42718972222"]
        tree = ET.parse(self.filtered_output_path)
        root = tree.getroot()

        for element in root.findall('Pod'):
            if element.text not in expected_elements:
                return False

        return True


if __name__ == '__main__':
    unittest.main()
