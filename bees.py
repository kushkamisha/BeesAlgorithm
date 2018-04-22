from Bees.aba import aba
import Bees.testFunctions as tf
from Bees.animation import animation


def main():
    # * n: number of agents
    # * function: test function
    # * lb: lower limits for plot axes
    # * ub: upper limits for plot axes
    # * dimension: space dimension
    # * iteration: number of iterations

    # Bees.aba(n, function, lb, ub, dimension, iteration)

    # easom_function
    # cross_in_tray_function
    # sphere_function
    # michalewicz_function
    # drop_wave_function

    bees = aba(15, tf.cross_in_tray_function, -20, 20, 2, 20)
    animation(bees.get_agents(), tf.cross_in_tray_function, -20, 20, True)

if __name__ == "__main__":
    main()
