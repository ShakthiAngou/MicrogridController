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
from supercapacitor import Supercapacitor

def main():
    """
    Run a 24-hour microgrid energy simulation.

    Simulates solar generation, load demand, and supercapacitor dispatch.
    """
    # Data being collected by simulation in lists
    hours_list = []
    solar_generated_list = []
    load_demand_list = []
    net_after_storage_list = []
    table_data = []
    supercapacitor = Supercapacitor(
        capacity_kwh = 25,
        initial_energy_kwh = 5
    )

    for hour in range(24):
        # Retrieve system variables
        solar_generated = get_solar(hour)
        load_demand = get_load(hour)
        net_power = calculate_net_energy(solar_generated, load_demand)

        # Each simulation step represents one hour, so kW of imbalance
        # over the step has the same numeric value in kWh.
        net_energy_kwh = net_power * 1.0
        energy_charged_kwh = 0.0
        energy_discharged_kwh = 0.0

        if net_energy_kwh > 0:
            energy_charged_kwh = supercapacitor.charge(net_energy_kwh)
        elif net_energy_kwh < 0:
            energy_discharged_kwh = supercapacitor.discharge(-net_energy_kwh)

        # Charging absorbs surplus; discharging supplies part of a deficit.
        # Remaining surplus is curtailed and remaining deficit is unserved.
        net_after_storage_kwh = (
            net_energy_kwh - energy_charged_kwh + energy_discharged_kwh
        )
        net_after_storage_power = net_after_storage_kwh / 1.0
        energy_status = determine_energy_status(net_after_storage_power)

        # Append inputs to data lists
        hours_list.append(hour)
        solar_generated_list.append(solar_generated)
        load_demand_list.append(load_demand)
        net_after_storage_list.append(net_after_storage_power)

        # Table data
        table_row = [
            hour,
            round(solar_generated, 2),
            round(load_demand, 2),
            round(net_power, 2),
            round(energy_charged_kwh, 2),
            round(energy_discharged_kwh, 2),
            round(net_after_storage_power, 2),
            round(supercapacitor.get_state_of_charge(), 1),
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
        colLabels=[
            'Hour', 'Solar (kW)', 'Load (kW)', 'Net Before Storage (kW)',
            'Charged (kWh)', 'Discharged (kWh)', 'Net After Storage (kW)',
            'SoC (%)', 'Status After Storage'
        ],
        loc='center'
    )

    # Graph
    graph_ax.set_title('Solar Generation and Load Demand Over 24 Hours')

    graph_ax.set_xlabel('Time of Day (h)')
    graph_ax.set_ylabel('Power (kW)')

    graph_ax.plot(hours_list, solar_generated_list, label='Solar Generated', color='orange')
    graph_ax.plot(hours_list, load_demand_list, label='Load Demand', color='blue')
    graph_ax.plot(
        hours_list,
        net_after_storage_list,
        label='Net Power After Storage',
        color='green',
        linestyle='--'
    )

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
