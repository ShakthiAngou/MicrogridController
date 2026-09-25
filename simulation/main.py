"""
main.py

Simulation entry point.

Runs the microgrid energy simulation, delegates dispatch decisions to the EMS,
and passes hourly results to the visualisation layer.
"""

from controller.energy_manager import EnergyManager
from visualisation.dashboard import show_simulation_dashboard

from .electrolyser import Electrolyser
from .fuel_cell import FuelCell
from .hydrogen import HydrogenStorage
from .load import get_load
from .solar import get_solar
from .supercapacitor import Supercapacitor


def main():
    """
    Run a 24-hour microgrid energy simulation.

    Retrieves simulated inputs, records EMS dispatch results, and displays the
    hourly dashboard.
    """

    # --- Data structure and initialisation ---

    # Step 1: set the timestep and prepare hourly results storage.
    time_step_hours = 1.0
    hourly_results = []

    # Step 2: Initialise the supercapacitor, hydrogen storage, electrolyser, and fuel cell.
    supercapacitor = Supercapacitor(capacity_kwh=25, initial_energy_kwh=15)
    hydrogen_storage = HydrogenStorage(capacity_kg=1.0, initial_hydrogen_kg=0.5)
    electrolyser = Electrolyser()
    fuel_cell = FuelCell()
    energy_manager = EnergyManager(
        supercapacitor,
        hydrogen_storage,
        electrolyser,
        fuel_cell,
    )

    # --- Simulation logic ---
    for hour in range(24):
        # Step 3: Retrieve simulated solar and load values.
        solar_generated = get_solar(hour)
        load_demand = get_load(hour)

        # Step 4: Ask the EMS to allocate energy across the storage systems.
        dispatch_result = energy_manager.dispatch(
            solar_generated,
            load_demand,
            time_step_hours,
        )

        # Step 5: Record the hourly EMS dispatch result.
        dispatch_result["hour"] = hour
        hourly_results.append(dispatch_result)

    # --- Output ---

    # Step 6: Pass the completed hourly results and initial capacities to the visualisation dashboard.
    show_simulation_dashboard(
        hourly_results,
        supercapacitor.capacity_kwh,
        hydrogen_storage.capacity_kg,
    )


if __name__ == "__main__":
    main()
