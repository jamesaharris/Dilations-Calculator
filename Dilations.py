#Garrett made the calculations, I made it clean and easy to run as a program.
while True:
    # x coord
    xP = input("Pre-Image X Coord:")
    x = int(xP)

    # y coord
    yP = input("Pre-Image Y Coord:")
    y = int(yP)

    # dilation factor
    dP = input("Dilation Factor:")
    d2 = str(dP)
    try:
        d = float(dP)
    except:
        one, two = d2.split("/")
        one1 = int(one)
        two2 = int(two)
        d = one1 / two2
    
    # x for center of dilation
    oP1 = input("Center of Dilation X:")
    o1 = int(oP1)

    # y for center of dilation
    oP2 = input("Center of Dilation Y:")
    o2 = int(oP2)

    # Dilation for a point calculations
    xs1 = x - o1
    ys1 = y - o2
    xs2 = xs1 * d
    ys2 = ys1 * d
    xs3 = xs2 + o1
    ys3 = ys2 + o2

    # Output
    print(f"({xs3} {ys3})")
    
    # Reset
    print("***New Calculation***")