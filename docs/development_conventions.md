# Development Conventions

# Virtual Environment

source venv/bin/activate

## Python Module Docstrings

All Python modules should include a module-level docstring.

Example:

"""
solar.py

Solar generation model.

Provides synthetic solar generation profiles
for the microgrid simulation environment.
"""

## Function Docstrings

Preferred sections:

- Args:
- Returns:
- Raises:
- Notes:
- Examples:
- Todo:

Example:

def get_solar(hour):
    """
    Calculate solar generation for a given hour.

    Args:
        hour (int): Hour of day [0-23].

    Returns:
        float: Solar generation in kW.

    Notes:
        Uses a sinusoidal profile to model daily
        solar generation.
    """