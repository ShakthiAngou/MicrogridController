# Development Conventions

# Virtual Environment

source venv/bin/activate

## Code Formatting and Linting

Run Ruff from the project root before committing or pushing changes.

```bash
ruff format simulation controller
ruff check simulation controller
```

Use the following command to apply automatic lint fixes, including import sorting:

```bash
ruff check --fix simulation controller
```

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
