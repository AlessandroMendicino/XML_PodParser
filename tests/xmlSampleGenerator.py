import xml.etree.ElementTree as ET
from xml.dom import minidom
from faker import Faker
import random

fake = Faker()

def prettify(elem):
    """Ritorna una stringa XML ben formattata"""
    rough_string = ET.tostring(elem, "utf-8")
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def generate_xml_sample(num_flows):
    root = ET.Element("FlussoMisure", xmlns="http://www.w3.org/2001/XMLSchema-instance", CodFlusso="PDO2G")

    for _ in range(num_flows):
        flow = ET.SubElement(root, "DatiPod")
        ET.SubElement(flow, "Pod").text = 'IT001E' + str(random.randint(10000000000, 99999999999))
        ET.SubElement(flow, "MeseAnno").text = fake.date_this_month().strftime("%m/%Y")

        dati_pdp = ET.SubElement(flow, "DatiPdp")
        ET.SubElement(dati_pdp, "Trattamento").text = random.choice(["O", "P"])
        ET.SubElement(dati_pdp, "Tensione").text = str(random.choice([220, 380, 400, 440]))
        ET.SubElement(dati_pdp, "Forfait").text = random.choice(["SI", "NO"])
        ET.SubElement(dati_pdp, "GruppoMis").text = random.choice(["SI", "NO"])
        ET.SubElement(dati_pdp, "Ka").text = "{:.3f}".format(random.uniform(20, 30))
        ET.SubElement(dati_pdp, "Kr").text = "{:.3f}".format(random.uniform(20, 30))
        ET.SubElement(dati_pdp, "Kp").text = "{:.3f}".format(random.uniform(20, 30))

        misura = ET.SubElement(flow, "Misura", xsi_type="DettaglioMisuraPeriodico2GORType")
        ET.SubElement(misura, "Raccolta").text = random.choice(["P", "T"])
        ET.SubElement(misura, "TipoDato").text = random.choice(["E", "F"])
        ET.SubElement(misura, "CausaOstativa").text = random.choice(["SI", "NO"])
        ET.SubElement(misura, "Validato").text = random.choice(["S", "N"])
        ET.SubElement(misura, "PotMax").text = "{:.3f}".format(random.uniform(0, 1))

        for i in range(1, min(16, random.randint(1, 16))): 
            ET.SubElement(misura, f"EaF{i}").text = "{:.3f}".format(random.uniform(0, 10))
            ET.SubElement(misura, f"ErF{i}").text = "{:.3f}".format(random.uniform(0, 10))

        ET.SubElement(misura, "Erc", Dst="0").text = "{:.3f}".format(random.uniform(0, 10))
        for i in range(1, min(16, random.randint(1, 16))): 
            ET.SubElement(misura, f"ErcF{i}").text = "{:.3f}".format(random.uniform(0, 10))

    xml_string = prettify(root)
    with open("./xml_files/generated_sample.xml", "wb") as file:
        file.write(xml_string.encode("utf-8"))

generate_xml_sample(5)
