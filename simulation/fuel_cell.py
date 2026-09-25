"""
fuel_cell.py

Fuel cell model.

Converts hydrogen mass into electrical energy using an idealized conversion.
"""


class FuelCell:
    """Convert hydrogen into electrical energy."""

    HYDROGEN_ENERGY_CONTENT_KWH_PER_KG = 33.33

    def generate_electricity(self, hydrogen_kg):
        """
        Calculate electrical energy generated from hydrogen.

        Args:
            hydrogen_kg (float): Hydrogen supplied in kg.

        Returns:
            float: Electrical energy generated in kWh.

        Notes:
            Assumes ideal conversion with no energy losses.
        """
        if hydrogen_kg < 0:
            raise ValueError("Hydrogen amount cannot be negative.")

        return hydrogen_kg * self.HYDROGEN_ENERGY_CONTENT_KWH_PER_KG
