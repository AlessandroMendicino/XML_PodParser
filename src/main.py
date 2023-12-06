import xml.etree.ElementTree as ET
from jproperties import Properties
from StrategyParserXML import SetParser
from StrategyParserXML import TreeStrategy, DomStrategy
#from parserXML import TreeParserFactory, DomParserFactory

 

def input_read():
    XML_INPUT_PATH = "./xml_files/05779711000_06655971007_202303_PDO2G_20230401145448_1DP1676_R.xml"
    DATETIME_TAG="MeseAnno"
    INPUT_FILTER="IT001E00000004=03/2023,IT001E00000757=03/2023-02/2023"
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






