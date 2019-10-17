from urllib.request import urlopen
import sys
import re

def getTextValue(text_file_url,text_attribute):
	data = urlopen(text_file_url) # parse the data
	text_values = ''.join(str(str(text_val).split("=")[1]).strip() for text_val in data if text_attribute+"=" in str(text_val)) #extract values
	values = [int_val.strip() for int_val in re.findall(r'\"(.+?)\"', text_values)] #get actual value within double quotes
	return values

if __name__ == '__main__':
	if len(sys.argv) == 3:
		text_file_url = str(sys.argv[1]).strip()
		text_attribute = str(sys.argv[2]).strip()
		try:
			text_values = getTextValue(text_file_url,text_attribute)
			if len(text_values) > 0:
				print(text_attribute,": ",' '.join(str(value) for value in text_values))
			else:
				print("No values found for tag",text_attribute," in ",text_file_url)
		except:
			print("Error in url ",text_file_url)
	else:
		print("Please enter two arguments i.e. python file_name url attribute, eg python textParser.py  http://www.quantum-simulation.org/potentials/sg15_oncv/upf/Ba_ONCV_PBE-1.0.upf z_valence")
		sys.exit()
	