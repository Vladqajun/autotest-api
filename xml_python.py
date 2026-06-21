import xml.etree.ElementTree as ET



with open('xml_example.xml', 'r', encoding='utf-8') as f:
    tree = ET.parse(f)
    root = tree.getroot()


print("User ID:", root.find('id').text)
print("User Name:", root.find('first_name').text, root.find('last_name').text)
print("User Email:", root.find('email').text)

