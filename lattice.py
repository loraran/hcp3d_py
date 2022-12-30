from numpy import zeros, linspace, meshgrid
from math import sqrt, floor

import logger


class Lattice:
    def __init__(self):
        self.atomic_number = 12  # fmg
        self.Q = 5.21
        self.in_plane_a = 3.2094
        self.in_plane_b = 3.2094
        self.in_plane_ab = 0  # assumes that in_plane_a != in_plane_b
        self.out_of_plane_c = 5.2108  # clatt


def get_box_size(number_particles):
    lattice = Lattice()
    num_part = number_particles ** 2  # nPart
    total_particles = floor(sqrt(num_part))  # intRoot

    check_perfect_square(num_part, total_particles)

    # Lattice parameters (separation length between atoms)
    if lattice.in_plane_a == lattice.in_plane_b:
        lattice.in_plane_ab = lattice.in_plane_a
        logger.info('In-plane lattice parameters are identical. Using in_plane_ab parameter.')

    separation_distance = lattice.in_plane_ab / lattice.Q  # sepDist

    # Find the box size
    lx = separation_distance * 1 * sqrt(num_part)  # Lx
    ly = lx * (sqrt(3) / 2)  # Ly

    # Create a vector of linearly spaced points along the x-direction
    # linspace(a,b,n) generates a row vector of n points linearly spaced between a and b
    x_positions = linspace(separation_distance / 2, (lx - separation_distance) / 2, 1 * sqrt(num_part))  # xPos
    # And find the corresponding y-direction increments
    y_positions = (sqrt(3) / 2) * x_positions  # yPos

    # Create a matrix with all combinations of x and y
    [x, y] = meshgrid(x_positions, y_positions)

    # TODO: adaptar expressão a seguir ao formato py
    # Shift coordinates to be at the center of each particle
    # x(1:2:len(x), :) = x(1:2:len(y), :) + separation_distance / 2

    max_z = x.shape().max(0)  # maxZ
    z = zeros(max_z, max_z) - num_part / 4  # Z

    # Reshape the matrix to be 1D in X and 1D in Y
    # (numel returns the number of elements in a given array)
    # coords = [reshape(X,1,numel(X)); reshape(Y,1,numel(Y))]; %#ok<NASGU>
    # X2 = X;
    # Y2 = Y + 0.5*sepDist;
    # Z2 = Z + 0.5;
    # % Z2 = Z + clatt/2;
    # %  plot3(X,Y,Z,'k.'); hold on;
    # %  plot3(X2,Y2,Z2,'r.'); hold off;
    # %  pause


def check_perfect_square(num_part, total_particles):
    if (sqrt(num_part) - total_particles) > 1e-7:
        logger.critical('Number of particles should be a perfect square!')
        zeros((2, num_part))
        lx = 0.0
        ly = 0.0
        return
