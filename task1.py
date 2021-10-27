from lxml import html, etree

with open (r"source\listing.html", "r") as file:
    page = file.read()
    file.close()
tree = html.fromstring(page)

Selector_1 = "ul.bloco-dados > li:nth-child(4) > span"
Selector_2 = "ul.bloco-dados > li:nth-child(5) > span"
Selector_3 = "ul.bloco-dados > li:nth-child(2) > span"
Selector_4 = "ul.bloco-dados > li:nth-child(6) > span"
Selector_5 = "div.bloco-imovel-texto > p"
Selector_6 = "div.info1 > div.lbl_titulo"
Selector_7 = "div.pnl_mapa > span.lbl_morada"

#Extra Challenge
Selector_extra_1 = "div#Cpl_modulocaracteristicas_div_caracteristicas_gerais > ul > li:nth-child(1) > span#features"
Selector_extra_2 = "div#Cpl_modulocaracteristicas_div_caracteristicas_gerais > ul > li:nth-child(2) > span#features"
Selector_extra_3 = "div#Cpl_modulocaracteristicas_div_caracteristicas_gerais > ul > li:nth-child(3) > span#features"
Selector_extra_4 = "div#Cpl_modulocaracteristicas_div_caracteristicas_gerais > ul > li:nth-child(4) > span#features"

print('Bathrooms: {}\n'.format(tree.cssselect(Selector_1)[0].text))
print('Bedrooms: {}\n'.format(tree.cssselect(Selector_2)[0].text))
print('Living area: {}\n'.format(tree.cssselect(Selector_3)[0].text))
print('Energy Rating: {}\n'.format(tree.cssselect(Selector_4)[0].text))
print('Description: {}\n'.format(tree.cssselect(Selector_5)[0].text))
print('Agent name: {}\n'.format(tree.cssselect(Selector_6)[0].text))
print('Location: {}\n'.format(tree.cssselect(Selector_7)[0].text))

print(f'Features : {tree.cssselect(Selector_extra_1)[0].text}, {tree.cssselect(Selector_extra_2)[0].text},'
      f' {tree.cssselect(Selector_extra_3)[0].text}, {tree.cssselect(Selector_extra_4)[0].text}')