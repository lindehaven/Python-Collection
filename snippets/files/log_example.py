# Vi importerar logging för att få tillgång till loggningsfunktionerna.
import logging

# Vi bestämmer oss för vilket format som varje rad i logg-filen ska ha. Det finns en
# hel del reserverade ord att välja mellan för att få loggningen som man vill, exvis
# '%(levelname)s' som är namnet på loggningsnivån som sträng och
# '%(lineno)d' som är radnumret i källkodsfilen som decimaltal.
# Exempel på ett användbart format: 
FORM = '%(asctime)-15s %(levelname)s in %(filename)s at line %(lineno)d : %(message)s'

# Vi konfigurerar namnet på logg-filen, nivån och formatet vi vill använda. Väljer vi
# den lägsta nivån DEBUG så kommer alla loggningar att sparas till fil.
logging.basicConfig(filename = 'log_example.log', level = logging.DEBUG, format = FORM)

# När vi skriver koden så bestämmer vi oss för vad som är viktigt att logga på olika
# nivåer. Vi har tillgång till nivåerna CRITICAL, ERROR, WARNING, INFO och DEBUG
# genom att anropa motsvarande funktion critical, error, warning, info och debug.
logging.critical('CRITICAL is for critical errors that cannot be resolved.')
logging.error('ERROR is for major errors.')
logging.warning('WARNING is for anomalies that might become errors.')
logging.info('INFO is for important states in normal operation.')
logging.debug('DEBUG is for trouble-shooting.')

# Innan vi sedan gör en release så kan vi ändra konfigurationen av nivån till ERROR.
# Då kommer endast CRITICAL och ERROR att loggas.
logging.basicConfig(filename = 'log_example.log', level = logging.ERROR, format = FORM)

logging.getLogger().setLevel(logging.ERROR)
logging.critical('Will be logged.')
logging.error('Will be logged.')
logging.warning('Will be logged.')
logging.info('Will not be logged.')
logging.debug('Will not be logged.')
