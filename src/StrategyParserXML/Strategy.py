import xml.etree.ElementTree as ET
from xml.dom import minidom 

#Strategy Pattern design for xmlParser

#strategy Interface
class ParsingStrategy():
    def parse(self, file_input, tag, filter_data):
        pass


#parsing and filter xml using elementTree
class TreeStrategy(ParsingStrategy):
    
    def parse(self, file_input, tag, filter_data):
        tree = ET.parse(file_input)
        root = tree.getroot()
        filter_dict = {pod: dates.split('-') for pod, dates in (item.split('=') for item in filter_data.split(','))}

        for element in root.findall('DatiPod'):
            pod = element.findtext('Pod')
            date = element.findtext(tag)

            if pod in filter_dict and date in filter_dict[pod]:
                continue
            else:
                root.remove(element)

        tree.write('filtered.xml')
        

class DomStrategy(ParsingStrategy):
    
    def parse(self, file_input, tag, filter_data):
        filter_dict = {pod: dates.split('-') for pod, dates in (item.split('=') for item in filter_data.split(','))}
        dom = minidom.parse(file_input)
        DatiPod = dom.getElementsByTagName('DatiPod')
        tags_to_remove = []

        for element in DatiPod:
            pod = element.getElementsByTagName('Pod')
            date = element.getElementsByTagName(tag)
            if pod[0].firstChild.data in filter_dict and date[0].firstChild.data in filter_dict[pod[0].firstChild.data]:
                continue
            else:
                tags_to_remove.append(element)

        for tag in tags_to_remove:
            tag.parentNode.removeChild(tag)

        with open('filtered.xml', 'w') as file:
            dom.writexml(file)
    
    
#contest
class SetParser():
    
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def parse_xml(self, file_input, tag, filter_data):
        self._strategy.parse(file_input, tag, filter_data)
    