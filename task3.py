import re

with open(r'source\sample.json', "r") as f:
    json = f.read()
    f.close()

Regexp = r"([A-Z]{2}\d{3})(?!.*\1)"
print('----- Expressions extracted -----')
print("First unique id: {}".format(re.findall(Regexp, json)[0]))
print("Last unique id: {}".format(re.findall(Regexp, json)[-1]))
print("Length of list of unique ids: {}".format(len(re.findall(Regexp, json))))