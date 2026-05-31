"""
load.py

Load demand model.

Provides a synthetic load profile for the microgrid simulation environment.

Pending work:
    - Integrate measures load demand input data
    - Model diurnal and seasonal demand variation
"""

def get_load(hour):
    """
    Calculate load demand for a given hour.

    Args:
        hour (int): Hour of day [0-23].

    Returns:
        float: Load demand in kW.

    Notes:
        - Demand peaks during morning and evening rush.

        00:00-05:00  low demand
        06:00-09:00  morning peak
        10:00-17:00  moderate demand
        18:00-22:00  evening peak
        23:00        decline

    """

    # Piecewise function that assumes that demand peaks during
    # morning and evening hours

    if 0 <= hour <= 5:
        return 2
    elif 6 <= hour <= 9:
        return 6
    elif 10 <= hour <= 17:
        return 4
    elif 18 <= hour <= 22:
        return 8
    else:
        return 3
