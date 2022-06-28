age = int(input("Ålder? "))
print("Jaha, du är", age, "år gammal.")
if age < 0:
    print("Nä du, du är inte född än!")
elif age < 6:
    print("Du har inte börjat skolan än")
elif age >= 13 and age <= 19:
    print("Du är tonåring")
    if age == 18:
        print("Du är nu myndig")
else:
    print("Du är vuxen")
