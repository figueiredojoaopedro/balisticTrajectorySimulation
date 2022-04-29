import math


def main():
    """
    Main function
    """
    # Inputs:
    y0 = float(input("Initial height (m): "))
    v0 = float(input("Initial velocity (m/s): "))
    launchAngle = float(input("Initial angle (degrees): "))
    td = float(input("Instant of time you want to know the stuff: "))

    # Constants:
    g = 9.81;

    # radians calculation:
    launchAngle = math.radians(launchAngle);

    # v0x, v0y
    v0x = vox(v0, launchAngle);
    v0y = voy(v0, launchAngle);
    print("%.2f" % v0x);
    print("%.2f" % v0y)

    # time the ball keeps in the air
    t = totalTime(v0, launchAngle, g)
    print("%.2f" % t)

    # position of the ball
    xd = positionX(v0x, td);
    yd = positionY(v0y, y0, g, td);
    print("%.2f" % xd);
    print("%.2f" % yd);

def vox(vo, theta):
    v0x = vo*(math.cos(theta));
    return v0x;

def voy(vo, theta):
    v0y = vo*(math.sin(theta));
    return v0y;

def totalTime(v0, theta, g):
    t = 2*(v0*(math.sin(theta)))/g;
    return t;

def positionX(v0x, td):
    x = (v0x*td);
    return x;
    
def positionY(v0y, y0, g, td):
    y = (y0 + (v0y*td) - (1/2)*g*td*td);
    return y;

main()
