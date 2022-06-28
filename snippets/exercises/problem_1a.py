#   Multiplikation av heltal kan ses som en upprepad addition. Exempelvis
#   är 3·5 = 5+5+5. Skriv ett program som beräknar produkten av två positiva
#   heltal med hjälp av addition.
#
# Analys
#   Vilka är indata?
#     Två tal a och b som kan matas in via tangentbordet.
#   Vilket resultat förväntas?
#     Produkten p av de två talen a och b där produkten beräknas genom
#     upprepad addition.
#   Vad behöver vi?
#     Inmatning av talen a och b.
#     En slinga som repeterar a gånger och adderar b till p.
#     Utskrift av p.
a = int(input('Det första talet: '))
b = int(input('Det andra talet: '))
p = 0
while a > 0:
    p = p + b
    a = a - 1
print(p)
