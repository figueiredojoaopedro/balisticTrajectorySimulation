import math


def main():
    """
    Main function
    """
    # Inputs:
    y0 = float(input("Initial height (m): "));
    v0 = float(input("Initial velocity (m/s): "));
    launchAngle = float(input("Initial angle (degrees): "));
    td = float(input("Instant of time you want to know the stuff: "));

    # Constants:
    g = 9.8;

    # radians calculation:
    launchAngle = math.radians(launchAngle);

    # v0x, v0y
    v0x = vox(v0, launchAngle);
    v0y = voy(v0, launchAngle);
    print("v0x = %.2f" % v0x);
    print("v0y = %.2f" % v0y);

    # time the projectile keeps in the air
    t = totalTime(v0, launchAngle, g);
    print("Tar = %.2f" % t);

    # position of the projectile by the time inputed
    xd = positionX(v0x, td);
    yd = positionY(v0y, y0, g, td);
    print("xd = %.2f" % xd);
    print("yd = %.2f" % yd);

    #velocity of the projectile at the instant of time inputed
    print("vx = %.2f" % v0x);
    print("vy = %.2f" % vy(v0,td, launchAngle, g));
    print("v = %.2f" % velocityModule(v0x, vy(v0,td, launchAngle, g)));

    # max height
    print("Max Height = %.2f" % maxHeight(v0, launchAngle, g));
    
    # max range
    print("Max Range = %.2f" % maxRange(v0x, t));

    # velocity before touching the ground
    print("vxTouch = %.2f" % vxTouch(v0, launchAngle));
    print("vyTouch = %.2f" % vyTouch(v0, launchAngle, g, t));
    print("vTouch = %.2f" % velocityModuleTouch(vxTouch(v0, launchAngle), vyTouch(v0, launchAngle, g, t)));
    
    # when the projectile is at max height
    print("vxMaxHeight = %.2f" % vxMaxHeight(v0, launchAngle));
    print("vyMaxHeight = %.2f" % vyMaxHeight(v0, launchAngle, g, t));
    print("vMaxHeight = %.2f" % vMaxHeight(vxMaxHeight(v0, launchAngle), vyMaxHeight(v0, launchAngle, g, t)));

# initial x velocity of the projectile
def vox(vo, theta):
    v0x = vo*(math.cos(theta));
    return v0x;

# initial y velocity of the projectile
def voy(vo, theta):
    v0y = vo*(math.sin(theta));
    return v0y;

# time the projectile keeps in the air
def totalTime(v0, theta, g):
    t = 2*(v0*(math.sin(theta)))/g;
    return t;

# position of the projectile by the time inputed
def positionX(v0x, td):
    x = (v0x*td);
    return x;
    
# position of the projectile by the time inputed
def positionY(v0y, y0, g, td):
    y = y0 + (v0y*td) - (g*(math.pow(td, 2)))/2;
    return y;
# y velocity of the projectile at the instant of time inputed
def vy(v0,td, theta, g):
    vy = v0*math.sin(theta) - g*td;
    return vy;
# velocity module of the projectile
def velocityModule(vx,vy):
    v = math.sqrt(math.pow(vx,2) + math.pow(vy,2));
    return v;

# max height the projectile reached
def maxHeight(v0, theta, g):
    maxHeight = ((1/2)*(pow(v0,2)*pow(math.sin(theta),2)))/g;
    return maxHeight;

# max reach/range of the projectile
def maxRange(v0x, tar):
    maxRange = v0x*tar;
    return maxRange;

# velocity x before touching the ground
def vxTouch(v0, theta):
    vxTouch = v0*math.cos(theta);
    return vxTouch;

# velocity y before touching the ground
def vyTouch(v0, theta, g, tar):
    vyTouch = v0*math.sin(theta) - g*tar;
    return vyTouch;

# velocity module before touching the ground
def velocityModuleTouch(vx,vy):
    v = math.sqrt(math.pow(vx,2) + math.pow(vy,2));
    return v;

# when the projectile is at max height
def vxMaxHeight(v0, theta):
    vx = v0*math.cos(theta);
    return vx;
def vyMaxHeight(v0, theta, g, tar):
    vy = v0*math.sin(theta) - g*(tar/2);
    return vy;
def vMaxHeight(vx, vy):
    v = math.sqrt(math.pow(vx,2) + math.pow(vy,2));
    return v;

main()
