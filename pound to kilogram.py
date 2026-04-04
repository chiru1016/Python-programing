w = input("wt is your weight? ")
parameter = input("(L)bs or (K)g?? ")
if parameter.upper()=="K":
    weight = float(w) *2
    print(f"weight is {weight}pounds ")
elif parameter.upper()=="L":
    weight = float(w) /2
    print(f"weight is {weight}KG")
else:
    print("invallid")
