from matplotlib import pyplot as plt
import math

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

def add_circle(fig, center, radius, color):
    circle = plt.Circle(center, radius, fill=False, linewidth=1, edgecolor=color)
    fig.gca().add_artist(circle)

def mounting_holes_circle(fig, radius, spacing):
    for i in range(0,3):
        add_circle(fig, (math.cos(2*i*math.pi/3+math.pi/2)*spacing/2, math.sin(2*i*math.pi/3+math.pi/2)*spacing/2), radius, 'blue')
    #add_circle(fig, (-spacing/2, 0), radius, 'blue')
    #add_circle(fig, (spacing / 2, 0), radius, 'blue')

def BigCircle(fig, radius, mh_radius, spacing):
    add_circle(fig, (0, 0), radius, 'red')
    mounting_holes_circle(fig, mh_radius, spacing)

def ActiveCircle(fig,radius):
    add_circle(fig, (0, 0), radius, 'cyan')

def add_square(fig, side, color):
    corner = side/2
    line = plt.Line2D([-corner, -corner], [corner, -corner], linestyle='-', color=color)
    fig.gca().add_artist(line)
    line = plt.Line2D([corner, -corner], [corner, corner], linestyle='-', color=color)
    fig.gca().add_artist(line)
    line = plt.Line2D([corner, corner], [-corner, corner], linestyle='-', color=color)
    fig.gca().add_artist(line)
    line = plt.Line2D([-corner, corner], [-corner, -corner], linestyle='-', color=color)
    fig.gca().add_artist(line)

def mounting_holes_square(fig, radius, spacing):
    add_circle(fig, (-spacing/2, -spacing/2), radius, 'blue')
    add_circle(fig, (-spacing / 2, spacing/2), radius, 'blue')
    add_circle(fig, (spacing / 2, spacing / 2), radius, 'blue')
    add_circle(fig, (spacing / 2, -spacing / 2), radius, 'blue')

def BigSquare(fig, side, radius, spacing):
    add_square(fig, side, 'red')
    mounting_holes_square(fig, radius, spacing)

def ActiveSquare(fig,side):
    add_square(fig, side, 'cyan')

def holePattern(fig, radius, spacing, rows):
    add_circle(fig, (0, 0), radius, 'green')
    x = []
    y = []
    for i in range(0, rows):
        for j in range(0,i*6):
            x.append(i*spacing*math.cos(j*math.pi/(3*i)))
            y.append(i*spacing*math.sin(j*math.pi/(3*i)))
    for i in range(0, len(x)):
        add_circle(fig, (x[i], y[i]), radius, 'green')