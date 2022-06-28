from subprocess import call
module = input('Vilken modul vill du installera? ')
try:
    call(['pip', 'install', module])
except Exception:
    print('Det gick inte att installera modulen', module, '!')
input('Tryck Enter för att avsluta.')
