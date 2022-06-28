import turtle              # Importera modulen.
t = turtle.Turtle()        # Turtle() skapar vår sköldpadda.
for i in range(4):         # Vi repeterar för varje sida av kvadraten.
   t.forward(50)           # Sköldpaddan går 50 små steg framåt.
   t.right(90)             # Sköldpaddan svänger 90 grader åt höger.
turtle.done()              # Sköldpaddan är färdig!
