import xml.etree.ElementTree as ET
from jproperties import Properties
from StrategyParserXML import SetParser
from StrategyParserXML import TreeStrategy, DomStrategy
#from parserXML import TreeParserFactory, DomParserFactory

 

def input_read():
    XML_INPUT_PATH = "./src/xml_files/generated_sample.xml"
    DATETIME_TAG="MeseAnno"
    INPUT_FILTER="IT001E42718972222=13/2023"
    return XML_INPUT_PATH, DATETIME_TAG, INPUT_FILTER

def choose_strategy():
    print("Select parsing strategy:")
    print("1. TreeStrategy")
    print("2. DomStrategy")
    choice = input("Insert number: ")
    if choice == "1":
        return TreeStrategy()
    elif choice == "2":
        return DomStrategy()
    else:
        print("no found strategy. TreeStrategy default.")
        return TreeStrategy()
    
    

XML_INPUT_PATH, DATETIME_TAG, INPUT_FILTER = input_read()

parser_ = SetParser(choose_strategy())

parser_.parse_xml(XML_INPUT_PATH, DATETIME_TAG, INPUT_FILTER)






