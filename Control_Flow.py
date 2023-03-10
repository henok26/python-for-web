Route1 = "Debremarkos To Addis Ababa"
Route2 = "Addis Ababa To Bahir Dar"
Route3 = "Addis Ababa To Gondar"
Bus_Id1 = "Fm1"
Bus_Id2 = "Fm2"
Bus_Id3 = "Fm3"
Bus_Id = input("enter bus id:")

if int(Bus_Id) == 1:
    print(Bus_Id1)
elif int(Bus_Id) == 2:
    print(Bus_Id2)
else:
    print(Bus_Id3)

message = "eligible" if int(Bus_Id) == 1 else "non eligble"
print(message)
