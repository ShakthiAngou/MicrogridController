"""
main.py

Simulation entry point.

Runs the microgrid simulation and displays system outputs.
"""

from solar import get_solar
import matplotlib.pyplot as matplot
import numpy as numpy

def main():
    """
    Run a 24-hour solar generation simulation.
    """
    hours_list = []
    solar_inputs_list = []
    for hour in range(24):
        solar_generation = get_solar(hour)

        hours_list.append(hour)
        solar_inputs_list.append(solar_generation)

        print(
            f"Hour {hour:02d}: "
            f"{solar_generation:.2f} kW"
        )

    # Graph with matplotlib
    figure, ax = matplot.subplots()

    ax.set_title('Daily Solar Generation')
    ax.set_xlabel('Time of Day (h)')
    ax.set_ylabel('Solar Generated (kW)')

    ax.plot(hours_list, solar_inputs_list)
    matplot.show()
    # Todo: Multicolorued line graph


if __name__ == "__main__":
    main()