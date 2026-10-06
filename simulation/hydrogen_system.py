"""
hydrogen_system.py

Hydrogen subsystem model.

Coordinates hydrogen storage, electrolysis, and fuel-cell conversion.
"""

from .electrolyser import Electrolyser
from .fuel_cell import FuelCell
from .hydrogen import HydrogenStorage


class HydrogenSubsystem:
    """
    Hydrogen storage and conversion subsystem.

    Owns the hydrogen storage inventory, electrolyser, and fuel cell so that
    the EMS does not need to manage their internal conversion calculations.
    """

    def __init__(self, capacity_kg, initial_hydrogen_kg):
        """
        Initialize the hydrogen subsystem.

        Args:
            capacity_kg (float): Maximum hydrogen storage capacity in kg.
            initial_hydrogen_kg (float): Initial hydrogen inventory in kg.
        """
        self.storage = HydrogenStorage(capacity_kg, initial_hydrogen_kg)
        self.electrolyser = Electrolyser()
        self.fuel_cell = FuelCell()

    @property
    def capacity_kg(self):
        """Return the hydrogen storage capacity in kg."""
        return self.storage.capacity_kg

    @property
    def current_hydrogen_kg(self):
        """Return the current hydrogen inventory in kg."""
        return self.storage.current_hydrogen_kg

    def store_surplus(self, energy_kwh):
        """
        Convert surplus electrical energy into stored hydrogen.

        Args:
            energy_kwh (float): Surplus electrical energy in kWh.

        Returns:
            dict: Hydrogen produced and electrical energy stored.
        """
        if energy_kwh < 0:
            raise ValueError("Surplus energy cannot be negative.")

        available_capacity_kg = (
            self.storage.capacity_kg - self.storage.current_hydrogen_kg
        )
        max_input_kwh = (
            available_capacity_kg * self.electrolyser.HYDROGEN_ENERGY_CONTENT_KWH_PER_KG
        )
        energy_to_electrolyser_kwh = min(energy_kwh, max_input_kwh)
        hydrogen_produced_kg = self.storage.store(
            self.electrolyser.produce_hydrogen(energy_to_electrolyser_kwh)
        )
        energy_stored_kwh = (
            hydrogen_produced_kg * self.electrolyser.HYDROGEN_ENERGY_CONTENT_KWH_PER_KG
        )

        return {
            "hydrogen_produced_kg": hydrogen_produced_kg,
            "energy_stored_kwh": energy_stored_kwh,
        }

    def supply_deficit(self, energy_kwh):
        """
        Convert stored hydrogen into electrical energy for a deficit.

        Args:
            energy_kwh (float): Electrical energy needed in kWh.

        Returns:
            dict: Hydrogen used and electrical energy supplied.
        """
        if energy_kwh < 0:
            raise ValueError("Deficit energy cannot be negative.")

        hydrogen_needed_kg = (
            energy_kwh / self.fuel_cell.HYDROGEN_ENERGY_CONTENT_KWH_PER_KG
        )
        hydrogen_used_kg = self.storage.withdraw(hydrogen_needed_kg)
        energy_supplied_kwh = self.fuel_cell.generate_electricity(hydrogen_used_kg)

        return {
            "hydrogen_used_kg": hydrogen_used_kg,
            "energy_supplied_kwh": energy_supplied_kwh,
        }

    def get_state_of_charge(self):
        """Return hydrogen inventory as a percentage of capacity."""
        return self.storage.get_state_of_charge()
