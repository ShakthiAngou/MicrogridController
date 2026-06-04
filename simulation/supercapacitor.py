"""
supercapacitor.py

Handles supercapacitor energy storage and management.
"""

class Supercapacitor:
    """
    Supercapacitor energy storage model.

    Attributes:
        capacity_kwh (float): Maximum energy storage capacity in kWh.
        current_energy_kwh (float): Current stored energy in kWh.

    """
    def __init__(self, capacity_kwh, initial_energy_kwh):
        """
        Initialize supercapacitor with specified capacity.

        Args:
            capacity_kwh (float): Maximum energy storage capacity in kWh.
        """
        self.capacity_kwh = capacity_kwh
        self.current_energy_kwh = initial_energy_kwh

    def charge(self, energy_kwh):
        """
        Charge the supercapacitor with specified energy.

        Args:
            energy_kwh (float): Energy to charge in kWh.

        Returns:
            float: Actual energy charged in kWh (may be less than requested if capacity is exceeded).
        """
        available_capacity = self.capacity_kwh - self.current_energy_kwh
        energy_to_charge = min(energy_kwh, available_capacity)
        self.current_energy_kwh += energy_to_charge
        return energy_to_charge

    def discharge(self, energy_kwh):
        """
        Discharge the supercapacitor by specified energy.

        Args:
            energy_kwh (float): Energy to discharge in kWh.

        Returns:
            float: Actual energy discharged in kWh (may be less than requested if not enough energy stored).
        """
        energy_to_discharge = min(energy_kwh, self.current_energy_kwh)
        self.current_energy_kwh -= energy_to_discharge
        return energy_to_discharge

    def get_state_of_charge(self):
        """
        Get the state of charge (SoC) of the supercapacitor as a percentage.

        Returns:
            float: State of charge in percentage (0-100%).
        """
        if self.capacity_kwh == 0:
            return 0.0
        return (self.current_energy_kwh / self.capacity_kwh) * 100
