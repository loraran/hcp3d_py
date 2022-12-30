import logger
import time
import lattice

# Gets current datetime at the start of execution:
start_time = time.time()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logger.config()

    print('- HCP LATTICE -')
    print('Define the crystal lattice by informing the square edge size in particles.')
    number_particles = int(input('  INPUT: '))
    logger.debug(f'number_particles = {number_particles}')

    lattice.get_box_size(number_particles)


# Calculates execution time of program:
end_time = time.time()
elapsed_time = end_time - start_time
logger.info(f'DONE - Total elapsed time is {elapsed_time} seconds.')
