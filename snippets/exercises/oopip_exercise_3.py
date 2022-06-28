def happy_day(day):
    if day == "monday":
        return ":("
    if day != "monday":
        return ":D"

print(happy_day("sunday"))
print(happy_day("monday"))
