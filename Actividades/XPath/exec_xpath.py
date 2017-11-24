from lxml import etree

doc = etree.parse('PCFactory.xml')

# Produce más de una impresora (count).
# s = "//Fabricante[count(Impresora)>1]/@nombre"

# Lo mismo sin count (PC).
# s = "//Fabricante[PC[following-sibling::PC]]/@nombre"

# Produce solamente una impresora.
# Esto está mal
# s = "//Fabricante[Impresora[not(following-sibling::Impresora)]]/@nombre"

# Produce solamente una impresora.
# Esto está bien
# s = ("//Fabricante[Impresora and "
#      + "not(Impresora[following-sibling::Impresora]) "
#      + "and not(Impresora[preceding-sibling::Impresora])]/@nombre")

# No quiero el computador con menos RAM. Quiero todos los demás.
# s = "//*[RAM > /Productos//*/RAM]/@modelo"

# Fabricantes con modelos en común
# s = "//*[@modelo = ../following-sibling::Fabricante/*/@modelo or @modelo = ../preceding-sibling::Fabricante/*/@modelo]/../@nombre"

# Fabricantes que produzcan PC
# s = "//PC/../@nombre"


# Producto que lo hacen dos fabricantes distintos
s = "//*[@modelo = ../following-sibling::Fabricante/*/@modelo]/@modelo"

# Todos los hijos de los nodos que contengan impresoras im3002
# s = "//Impresora[@modelo='im3002']/../*/@modelo"


for a in doc.xpath(s):
    print(a)
