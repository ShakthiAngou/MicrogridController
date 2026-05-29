"""
solar.py

Solar generation model.

Provides synthetic solar power generation profiles
for microgrid simulation environment.

Pending work:
    - Weather effects
    - Seasonal variation
    - Real solar datasets
"""

import math

def get_solar(hour):
    """
    Calculate solar generation for a given hour.

    Args:
        hour (int): Hour of day [0-23].

    Returns:
        float: Solar generation in kW.

    Notes:
        - Solar production occurs between 06:00 and 18:00.
        - Generation follows a sinusoidal profile.
        - Peak generation occurs at midday.

        00:00 - 06:00 -> 0 kW
        12:00         -> 10 kW
        18:00 - 23:00 -> 0 kW

    """

    # Assume sunrise at 06:00 and sunset at 18:00
    if 6 <= hour <= 18:
        return 10 * math.sin(math.pi * (hour - 6) / 12)

    return 0
