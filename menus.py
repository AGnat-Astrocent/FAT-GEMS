from plotter import * #add_circle, BigCircle
from dxf import *
def menu(fig):
    doc, msp = create_doc()

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

    print("Mounting hole diameter: ")
    mh_diameter = float(input())

    print("Mounting hole spacing: ")
    mh_spacing = int(input())

    match choice:
        case 1:
            print("Square")
            BigSquare(fig, msp, diameter, mh_diameter/2, mh_spacing)
            holePatternSquare(fig, msp, h_diameter/2,h_spacing,active)
            ActiveSquare(fig, msp, active)
        case 2:
            print("Circle")
            BigCircle(fig, msp, diameter/2, mh_diameter/2, mh_spacing)
            holePatternCircle(fig, msp, h_diameter / 2, h_spacing, active/2)
            ActiveCircle(fig, msp, active/2)
        case _:
            add_circle(fig, msp, (0,0), h_diameter/2,'red')
            mounting_holes(fig, msp, mh_diameter/2,'blue', mh_spacing)

    doc.saveas('T1.dxf')