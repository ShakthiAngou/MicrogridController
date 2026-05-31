"""
energy_balance.py

Energy balance model.

Provides net energy calculations and surplus/deficit
classification for the microgrid simulation.

Pending work:
    - Enum for energy status
"""


def calculate_net_energy(solar, load):
    """
    Calculates net energy of the system (input - output: solar - load)

    Args:
        solar (float): solar generated in kW
        load (float): load demand in kW

    Returns:
        float: signed net energy balance in kW

    Notes:
        - Positive net energy indicates surplus generation
        - Negative net energy indicates energy deficit
        - Zero indicates balanced generation and demand

    """
    return solar - load

def determine_energy_status(net_energy):
    """
    Output energy status of the system.

    Args:
        net_energy (float): net energy flow of system

    Returns:
        str: Energy status of the system. (SURPLUS | DEFICIT | BALANCED)

    Notes:
        net_energy > 0  => SURPLUS
        net_energy < 0  => DEFICIT
        net_energy = 0  => BALANCED

    """
    if net_energy > 0:
        return "SURPLUS"
    elif net_energy < 0:
        return "DEFICIT"
    else:
        return "BALANCED"