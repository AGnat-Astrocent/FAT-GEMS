from plotter import * #add_circle, BigCircle

def menu(fig):
    print("1. Square\n2. Circle")
    choice = int(input())

    print("Diameter/Side: ")
    diameter = int(input())

    print("Active diameter/side: ")
    active = int(input())

    print("Hole diameter: ")
    h_diameter = int(input())

    print("Hole spacing: ")
    h_spacing = int(input())

    print("Hole rows: ")
    h_rows = int(input())

    print("Mounting hole diameter: ")
    mh_diameter = int(input())

    print("Mounting hole spacing: ")
    mh_spacing = int(input())

    match choice:
        case 1:
            print("Square")
            BigSquare(fig, diameter, mh_diameter/2, mh_spacing)
            holePattern(fig,h_diameter/2,h_spacing,h_rows)
            ActiveSquare(fig,active)
        case 2:
            print("Circle")
            BigCircle(fig, diameter/2, mh_diameter/2, mh_spacing)
            holePattern(fig, h_diameter / 2, h_spacing, h_rows)
            ActiveCircle(fig, active/2)
        case _:
            add_circle(fig,(0,0), h_diameter/2,'red')
            mounting_holes(fig,mh_diameter/2,'blue', mh_spacing)

