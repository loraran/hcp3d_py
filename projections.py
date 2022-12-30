from math import pi, cos, sin
import lattice

def project_100():

    # (1 0 0) Projection - Rotation of crystal matrix
    theta_100 = 90
    thetarad_100 = theta_100 * (pi/180)

    # Rotation around Z-axis
    X_axis_100 = (lattice.atomlist(:,1) * cos(thetarad_100)) - (lattice.atomlist(:,2) * sin(thetarad_100))
    Y_axis_100 = (lattice.atomlist(:,1) * sin(thetarad_100)) - (lattice.atomlist(:,2) * cos(thetarad_100))
    Z_axis_100 = lattice.atomlist(:,3)
