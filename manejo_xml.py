# Código para manejar archivos XML
import xml.etree.ElementTree as ET

tree = ET.parse('archivo.xml')
root = tree.getroot()
for child in root:
    print(child.tag, child.attrib)

root = ET.Element("personas")
persona = ET.SubElement(root, "persona", nombre="Ana", edad="25")
tree = ET.ElementTree(root)
tree.write("archivo.xml")
