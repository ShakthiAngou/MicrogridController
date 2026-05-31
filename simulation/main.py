"""
main.py

Simulation entry point.

Runs the microgrid simulation and displays system outputs.
"""

import matplotlib.pyplot as matplot

from solar import get_solar
from load import get_load
from energy_balance import calculate_net_energy
from energy_balance import determine_energy_status

def main():
    """
    Run a 24-hour microgrid energy simulation.

    Simulates solar generation, load demand, and net energy balance.
    """
    # Data being collected by simulation in lists
    hours_list = []
    solar_generated_list = []
    load_demand_list = []
    net_energy_list = []
    energy_status_list = []
    table_data = []

    for hour in range(24):
        # Retrieve system variables
        solar_generated = get_solar(hour)
        load_demand = get_load(hour)
        net_energy = calculate_net_energy(solar_generated, load_demand)
        energy_status = determine_energy_status(net_energy)

        # Append inputs to data lists
        hours_list.append(hour)
        solar_generated_list.append(solar_generated)
        load_demand_list.append(load_demand)
        net_energy_list.append(net_energy)
        energy_status_list.append(energy_status)

        # Table data
        table_row = [
            hour,
            round(solar_generated, 2),
            round(load_demand, 2),
            round(net_energy, 2),
            energy_status
        ]
        table_data.append(table_row)

    # Visualise with matplotlib
    figure, (table_ax, graph_ax) = matplot.subplots(
        2, 1,
        figsize=(12, 8),
        gridspec_kw={'height_ratios': [1, 3]}
    )

    # Table
    table_ax.axis('off')
    table_ax.table(
        cellText=table_data,
        colLabels=['Hour', 'Solar Generated (kW)', 'Load Demand (kW)', 'Net Energy (kW)', 'Energy Status'],
        loc='center'
    )

    # Graph
    graph_ax.set_title('Solar Generation and Load Demand Over 24 Hours')

    graph_ax.set_xlabel('Time of Day (h)')
    graph_ax.set_ylabel('Power (kW)')

    graph_ax.plot(hours_list, solar_generated_list, label='Solar Generated', color='orange')
    graph_ax.plot(hours_list, load_demand_list, label='Load Demand', color='blue')

    graph_ax.grid(
        True,
        linestyle='--',
        alpha=0.7
    ) # Adding grid for better readability
    graph_ax.legend(loc='upper right')

    matplot.tight_layout()
    matplot.show()

    # Todo: Improve plots to be more visually appealing and informative


if __name__ == "__main__":
    main()