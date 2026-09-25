"""
hydrogen.py

Hydrogen storage model.

Tracks hydrogen inventory for long-duration energy storage.
"""


class HydrogenStorage:
    """
    Hydrogen storage inventory.

    Attributes:
        capacity_kg (float): Maximum hydrogen storage capacity in kg.
        current_hydrogen_kg (float): Current hydrogen inventory in kg.
    """

    def __init__(self, capacity_kg, initial_hydrogen_kg):
        """
        Initialize hydrogen storage.

        Args:
            capacity_kg (float): Maximum hydrogen storage capacity in kg.
            initial_hydrogen_kg (float): Initial hydrogen inventory in kg.
        """
        if capacity_kg < 0:
            raise ValueError("H2 storage capacity cannot be negative.")
        if not 0 <= initial_hydrogen_kg <= capacity_kg:
            raise ValueError(
                "Initial H2 inventory must be between zero and capacity, inclusive."
            )

        self.capacity_kg = capacity_kg
        self.current_hydrogen_kg = initial_hydrogen_kg

    def store(self, hydrogen_kg):
        """
        Add hydrogen to storage, up to its remaining capacity.

        Args:
            hydrogen_kg (float): Hydrogen to store in kg.

        Returns:
            float: Actual hydrogen stored in kg (may be less than requested if capacity is exceeded).
        """
        if hydrogen_kg < 0:
            raise ValueError("H2 amount to store cannot be negative.")

        available_capacity = self.capacity_kg - self.current_hydrogen_kg
        hydrogen_to_store = min(hydrogen_kg, available_capacity)
        self.current_hydrogen_kg += hydrogen_to_store
        return hydrogen_to_store

    def withdraw(self, hydrogen_kg):
        """
        Remove hydrogen from storage, up to the available inventory.

        Args:
            hydrogen_kg (float): Hydrogen to withdraw in kg.

        Returns:
            float: Actual hydrogen withdrawn in kg.
        """
        if hydrogen_kg < 0:
            raise ValueError("H2 amount to withdraw cannot be negative.")

        hydrogen_to_withdraw = min(hydrogen_kg, self.current_hydrogen_kg)
        self.current_hydrogen_kg -= hydrogen_to_withdraw
        return hydrogen_to_withdraw

    def get_state_of_charge(self):
        """
        Calculate hydrogen inventory as a percentage of capacity.

        Returns:
            float: State of charge as a percentage (0-100%).
        """
        if self.capacity_kg == 0:
            return 0.0
        return (self.current_hydrogen_kg / self.capacity_kg) * 100
