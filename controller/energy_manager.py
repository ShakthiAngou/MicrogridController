"""
energy_manager.py

V1: Rule-based Energy Management System.

Coordinates energy allocation across the supercapacitor and
hydrogen subsystem.
"""

from .energy_balance import (
    calculate_net_energy,
    determine_energy_status,
)


class EnergyManager:
    """
    Rule-based EMS controller.

    Uses the supercapacitor before hydrogen storage for both
    surplus and deficit conditions.
    """

    def __init__(
        self,
        supercapacitor,
        hydrogen_system,
    ):
        """
        Initialize the EMS with the available storage components.
        """
        self.supercapacitor = supercapacitor
        self.hydrogen_system = hydrogen_system

    def dispatch(self, solar_power_kw, load_power_kw, time_step_hours):
        """
        Allocate energy for one simulation timestep.

        Args:
            solar_power_kw (float): Solar generation in kW.
            load_power_kw (float): Load demand in kW.
            time_step_hours (float): Duration of the timestep in hours.

        Returns:
            dict: Hourly energy flows, storage levels, and system status.
        """
        net_power_kw = calculate_net_energy(solar_power_kw, load_power_kw)
        net_energy_kwh = net_power_kw * time_step_hours

        supercapacitor_charged_kwh = 0.0
        supercapacitor_discharged_kwh = 0.0
        hydrogen_produced_kg = 0.0
        hydrogen_used_kg = 0.0
        hydrogen_energy_kwh = 0.0

        # Step 1: Route surplus to the supercapacitor, then the electrolyser.
        if net_energy_kwh > 0:
            supercapacitor_charged_kwh = self.supercapacitor.charge(net_energy_kwh)
            remaining_surplus_kwh = net_energy_kwh - supercapacitor_charged_kwh

            hydrogen_result = self.hydrogen_system.store_surplus(remaining_surplus_kwh)
            hydrogen_produced_kg = hydrogen_result["hydrogen_produced_kg"]
            hydrogen_energy_kwh = hydrogen_result["energy_stored_kwh"]

        # Step 2: Cover deficits with the supercapacitor, then the fuel cell.
        elif net_energy_kwh < 0:
            supercapacitor_discharged_kwh = self.supercapacitor.discharge(
                -net_energy_kwh
            )
            remaining_deficit_kwh = -net_energy_kwh - supercapacitor_discharged_kwh

            hydrogen_result = self.hydrogen_system.supply_deficit(remaining_deficit_kwh)
            hydrogen_used_kg = hydrogen_result["hydrogen_used_kg"]
            hydrogen_energy_kwh = hydrogen_result["energy_supplied_kwh"]

        # Step 3: Calculate the remaining balance and classify the system state.
        # Remaining surplus is curtailed; remaining deficit is unserved.
        net_after_storage_kwh = (
            net_energy_kwh - supercapacitor_charged_kwh + supercapacitor_discharged_kwh
        )

        if net_energy_kwh > 0:
            net_after_storage_kwh -= hydrogen_energy_kwh
        elif net_energy_kwh < 0:
            net_after_storage_kwh += hydrogen_energy_kwh

        # Avoid classifying floating-point rounding residue as an imbalance.
        if abs(net_after_storage_kwh) < 1e-9:
            net_after_storage_kwh = 0.0

        net_after_storage_kw = net_after_storage_kwh / time_step_hours

        # Step 4: Return hourly energy flows and storage levels.
        return {
            "solar_power_kw": solar_power_kw,
            "load_power_kw": load_power_kw,
            "net_before_storage_kw": net_power_kw,
            "supercapacitor_charged_kwh": supercapacitor_charged_kwh,
            "supercapacitor_discharged_kwh": (supercapacitor_discharged_kwh),
            "hydrogen_produced_kg": hydrogen_produced_kg,
            "hydrogen_used_kg": hydrogen_used_kg,
            "net_after_storage_kw": net_after_storage_kw,
            "supercapacitor_energy_kwh": (self.supercapacitor.current_energy_kwh),
            "supercapacitor_soc_percent": (self.supercapacitor.get_state_of_charge()),
            "hydrogen_inventory_kg": self.hydrogen_system.current_hydrogen_kg,
            "hydrogen_soc_percent": self.hydrogen_system.get_state_of_charge(),
            "energy_status": determine_energy_status(net_after_storage_kw),
        }
