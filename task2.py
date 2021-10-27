import re

with open(r'source\listing.html', "r") as f:
    page = f.read()
    f.close()

Regexp_Phone_Number = r"[0-9]{4}-[0-9]{4}"
Regexp_Price = r"[0-9].[0-9]{3}.[0-9]{3}"
print("Phone number: {}".format(re.findall(Regexp_Phone_Number, page)[0]))
print(f"Price : {re.findall(Regexp_Price, page)[0]}")
