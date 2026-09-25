"""
electrolyser.py

Electrolyser model.

Converts electrical energy into hydrogen mass using an idealized conversion.
"""


class Electrolyser:
    """Convert electrical energy into hydrogen."""

    HYDROGEN_ENERGY_CONTENT_KWH_PER_KG = 33.33

    def produce_hydrogen(self, energy_kwh):
        """
        Calculate hydrogen produced from electrical energy.

        Args:
            energy_kwh (float): Electrical energy supplied in kWh.

        Returns:
            float: Hydrogen produced in kg.

        Notes:
            Assumes ideal conversion with no energy losses.
        """
        if energy_kwh < 0:
            raise ValueError("Input energy cannot be negative.")

        return energy_kwh / self.HYDROGEN_ENERGY_CONTENT_KWH_PER_KG
