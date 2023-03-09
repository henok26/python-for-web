Route1 = "Debremarkos to Addis Ababa"
PlateNo = 1234
Distance = 299.9
Escape = "welcome to \"fm\""
IsAvailableAfterNoon = False
print(Route1)
print(len(Route1))
print(Route1[-2])
print(Route1[-5])
print(Route1[0:11])
print(Route1[:])
print(Route1[:11])
print(Route1[0:])
print(Escape)
Format = f"{Route1}{Distance} {Escape}"
print(Format)
print(Route1.upper())
print(Route1.strip())
print(Route1.find("to"))
print(Route1.replace("to", "TO"))
print("to" in Route1)
BusId = input("BusId:")
print(int(BusId)+3)
print(f"x:{Route1}{Escape}")
