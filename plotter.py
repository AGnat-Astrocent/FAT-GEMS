from matplotlib import pyplot as plt
import math
from dxf import *

def plot_basis(size, title):
    # Plot to see what's happening
    fig,ax = plt.subplots(figsize=(size, size))
    plt.title(title)
    plt.xlim(-size, size)
    plt.ylim(-size, size)
    ax.xaxis.set_major_locator(plt.MultipleLocator(1))
    ax.yaxis.set_major_locator(plt.MultipleLocator(1))

    # Add minor ticks
    ax.xaxis.set_minor_locator(plt.MultipleLocator(0.5))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(0.5))

    # Customize grid appearance
    ax.grid(which='major', linestyle='-', linewidth='0.25', color='k')
    ax.grid(which='minor', linestyle='--', linewidth='0.125', color='k')

    #plt.show()

    return fig

def show_plot():
    plt.show()

def add_circle(fig,msp, center, radius, color,layer):
    circle = plt.Circle(center, radius, fill=False, linewidth=1, edgecolor=color)
    fig.gca().add_artist(circle)
    dxf_circle(msp,center,radius,layer)

def mounting_holes_circle(fig,msp, radius, spacing):
    for i in range(0,3):
        add_circle(fig, msp,(math.cos(2*i*math.pi/3+math.pi/2)*spacing/2, math.sin(2*i*math.pi/3+math.pi/2)*spacing/2), radius, 'blue',"Hole")

    #add_circle(fig, (-spacing/2, 0), radius, 'blue')
    #add_circle(fig, (spacing / 2, 0), radius, 'blue')

def BigCircle(fig,msp, radius, mh_radius, spacing):
    add_circle(fig, msp,(0, 0), radius, 'red',"Shape")
    mounting_holes_circle(fig, msp, mh_radius, spacing)

def ActiveCircle(fig,msp,radius):
    add_circle(fig, msp,(0, 0), radius, 'cyan', "Active")

def add_square(fig,msp, side, color,layer):
    corner = side/2
    line = plt.Line2D([-corner, -corner], [corner, -corner], linestyle='-', color=color)
    fig.gca().add_artist(line)
    line = plt.Line2D([corner, -corner], [corner, corner], linestyle='-', color=color)
    fig.gca().add_artist(line)
    line = plt.Line2D([corner, corner], [-corner, corner], linestyle='-', color=color)
    fig.gca().add_artist(line)
    line = plt.Line2D([-corner, corner], [-corner, -corner], linestyle='-', color=color)
    fig.gca().add_artist(line)
    dxf_square(msp,corner,layer)

def mounting_holes_square(fig, msp, radius, spacing):
    add_circle(fig, msp,(-spacing/2, -spacing/2), radius, 'blue', "Hole")
    add_circle(fig, msp,(-spacing / 2, spacing/2), radius, 'blue',"Hole")
    add_circle(fig, msp,(spacing / 2, spacing / 2), radius, 'blue', "Hole")
    add_circle(fig, msp,(spacing / 2, -spacing / 2), radius, 'blue',"Hole")

def BigSquare(fig, msp, side, radius, spacing):
    add_square(fig, msp,side, 'red',"Shape")
    mounting_holes_square(fig,msp, radius, spacing)

def ActiveSquare(fig,msp, side):
    add_square(fig, msp, side, 'cyan', "Active")

def holePatternCircle(fig,msp,radius,spacing,active_radius):
    add_circle(fig, msp, (0, 0), radius, 'green', "Pattern")
    x = []
    y = []
    distance = 0
    count = 0
    while (distance) <= active_radius:
        for j in range(0, count * 6):
            x.append(count * spacing * math.cos(j * math.pi / (3 * count)))
            y.append(count * spacing * math.sin(j * math.pi / (3 * count)))
            distance = math.sqrt(x[j] ** 2 + y[j] ** 2)
        count += 1

    for i in range(0, len(x)):
        distance = math.sqrt(x[i] ** 2 + y[i] ** 2)
        if (distance) <= active_radius:
            add_circle(fig, msp,(x[i], y[i]), radius, 'green', "Pattern")


def holePatternSquare(fig, msp, radius, spacing, active):
    add_circle(fig, msp, (0, 0), radius, 'green', "Pattern")
    x = []
    y = []
    distance = 0
    count = 0
    while (distance + radius) <= active:
        for j in range(0, count * 6):
            x.append(count * spacing * math.cos(j * math.pi / (3 * count)))
            y.append(count * spacing * math.sin(j * math.pi / (3 * count)))
            distance = math.sqrt(x[j] ** 2 + y[j] ** 2)
        count += 1

    for i in range(0, len(x)):
        distance = math.sqrt(x[i] ** 2 + y[i] ** 2)

        if(math.fabs(x[i]) + radius <= active/2 and math.fabs(y[i]) + radius <= active/2):
            add_circle(fig, msp, (x[i], y[i]), radius, 'green', "Pattern")
