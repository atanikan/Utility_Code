import xml.etree.ElementTree as ET
from urllib.request import urlopen
import sys

def getXMLValue(xml_file_url,xml_attribute):
	tree = ET.parse(urlopen(xml_file_url)) # parse the data
	root = tree.getroot()
	xml_values = [str(xml_val.text).strip() for xml_val in root.iter(xml_attribute)] #get values
	return xml_values

if __name__ == '__main__':
	if len(sys.argv) == 3:
		xml_file_url = str(sys.argv[1]).strip()
		xml_attribute = str(sys.argv[2]).strip()
		try:
			xml_values = getXMLValue(xml_file_url,xml_attribute)
			if len(xml_values) > 0:
				print(xml_attribute,": ",' '.join(str(value) for value in xml_values))
			else:
				print("No values found for tag",xml_attribute," in ",xml_file_url)
		except:
			print("Error in url ",xml_file_url)
	else:
		print("Please enter two arguments i.e. python file_name url attribute, eg python xmlParser.py  http://www.quantum-simulation.org/potentials/sg15_oncv/xml/Ba_ONCV_PBE-1.0.xml valence_charge")
		sys.exit()
	