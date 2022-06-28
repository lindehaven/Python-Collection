#   Undersök vilka tal från och med 1 till och med 20 som är jämna.
#
# Analys
#   Vilka är indata?
#     Två tal 1 och 20.
#   Vilket resultat förväntas?
#     Alla jämna tal från och med 1 till och med 20.
#   Vad behöver vi?
#     Om vi dividerar ett jämnt tal med 2 så får vi ett heltal utan decimaler.
#     Om vi dividerar ett udda tal med 2 kommer vi däremot alltid att få ett
#     decimaltal som svar (det kommer att sluta på ,5). För att undersöka om
#     svaret blir ett heltal jämför vi svaret med och utan decimaler. Om dessa
#     två är lika är det ett heltal.
# Skapa en ny fil för att prova något av följande lösningsförslag:
for n in range(1, 21):
    q = n / 2
    if q == int(q):
        print(n)
