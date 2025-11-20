import xml.etree.ElementTree as ET

try:
    tree = ET.parse('kraj.xml')
    root = tree.getroot()

    for child in root:
        print(f'tag: {child.tag}, atrybuty: {child.attrib}, tekst: {child.text}')

    print(f"dane z konkretnego węzła: {root[0]}")
    print(f"dane z konkretnego węzła: {root[0][1]}")
    print(f"dane z konkretnego węzła: {root[0][1].text}")
except Exception as e:
    print(e)

