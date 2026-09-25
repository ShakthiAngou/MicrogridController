"""
main.py

Simulation entry point.

Runs the microgrid energy simulation and passes its hourly results to the
visualization module.
"""

from electrolyser import Electrolyser
from energy_balance import calculate_net_energy, determine_energy_status
from fuel_cell import FuelCell
from hydrogen import HydrogenStorage
from load import get_load
from solar import get_solar
from supercapacitor import Supercapacitor

from visualisation import show_simulation_dashboard


def main():
    """
    Run a 24-hour microgrid energy simulation.

    Dispatches energy across solar generation, load demand, a supercapacitor,
    and hydrogen storage, then displays the hourly results.
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

    # --- Simulation logic ---
    for hour in range(24):
        # Step 3: Retrieve simulated solar and load values, then calculate the net energy.
        solar_generated = get_solar(hour)
        load_demand = get_load(hour)
        net_power = calculate_net_energy(solar_generated, load_demand)
        net_energy_kwh = net_power * time_step_hours

        energy_charged_kwh = 0.0
        energy_discharged_kwh = 0.0
        hydrogen_produced_kg = 0.0
        hydrogen_used_kg = 0.0
        hydrogen_energy_kwh = 0.0

        # Energy Status: SURPLUS
        if net_energy_kwh > 0:
            # Step 4: Route surplus to the supercapacitor, then the electrolyser.
            energy_charged_kwh = supercapacitor.charge(net_energy_kwh)
            remaining_surplus_kwh = net_energy_kwh - energy_charged_kwh

            # Use the electrolyser for surplus the supercapacitor cannot hold.
            available_hydrogen_capacity_kg = (
                hydrogen_storage.capacity_kg - hydrogen_storage.current_hydrogen_kg
            )
            max_electrolyser_input_kwh = (
                available_hydrogen_capacity_kg
                * electrolyser.HYDROGEN_ENERGY_CONTENT_KWH_PER_KG
            )
            energy_to_electrolyser_kwh = min(
                remaining_surplus_kwh, max_electrolyser_input_kwh
            )
            hydrogen_produced_kg = hydrogen_storage.store(
                electrolyser.produce_hydrogen(energy_to_electrolyser_kwh)
            )
            hydrogen_energy_kwh = (
                hydrogen_produced_kg * electrolyser.HYDROGEN_ENERGY_CONTENT_KWH_PER_KG
            )

        # Energy Status: DEFICIT
        elif net_energy_kwh < 0:
            # Step 5: Cover deficits with the supercapacitor, then the fuel cell.
            energy_discharged_kwh = supercapacitor.discharge(-net_energy_kwh)
            remaining_deficit_kwh = -net_energy_kwh - energy_discharged_kwh

            # Use stored hydrogen for any deficit left after supercapacitor dispatch.
            hydrogen_needed_kg = (
                remaining_deficit_kwh / fuel_cell.HYDROGEN_ENERGY_CONTENT_KWH_PER_KG
            )
            hydrogen_used_kg = hydrogen_storage.withdraw(hydrogen_needed_kg)
            hydrogen_energy_kwh = fuel_cell.generate_electricity(hydrogen_used_kg)

        # Step 6: Calculate the remaining balance and classify the system state.
        # Remaining surplus is curtailed; remaining deficit is unserved.
        net_after_storage_kwh = (
            net_energy_kwh - energy_charged_kwh + energy_discharged_kwh
        )
        if net_energy_kwh > 0:
            net_after_storage_kwh -= hydrogen_energy_kwh
        elif net_energy_kwh < 0:
            net_after_storage_kwh += hydrogen_energy_kwh

        # Avoid classifying floating-point rounding residue as an imbalance.
        if abs(net_after_storage_kwh) < 1e-9:
            net_after_storage_kwh = 0.0

        # Step 7: Record hourly energy flows and storage levels.
        net_after_storage_power = net_after_storage_kwh / time_step_hours
        energy_status = determine_energy_status(net_after_storage_power)

        hourly_results.append(
            {
                "hour": hour,
                "solar_power_kw": solar_generated,
                "load_power_kw": load_demand,
                "net_before_storage_kw": net_power,
                "supercapacitor_charged_kwh": energy_charged_kwh,
                "supercapacitor_discharged_kwh": energy_discharged_kwh,
                "hydrogen_produced_kg": hydrogen_produced_kg,
                "hydrogen_used_kg": hydrogen_used_kg,
                "net_after_storage_kw": net_after_storage_power,
                "supercapacitor_energy_kwh": supercapacitor.current_energy_kwh,
                "supercapacitor_soc_percent": supercapacitor.get_state_of_charge(),
                "hydrogen_inventory_kg": hydrogen_storage.current_hydrogen_kg,
                "hydrogen_soc_percent": hydrogen_storage.get_state_of_charge(),
                "energy_status": energy_status,
            }
        )

    # --- Output ---

    # Step 8: Pass the completed hourly results and initial capacities to the visualisation dashboard.
    show_simulation_dashboard(
        hourly_results,
        supercapacitor.capacity_kwh,
        hydrogen_storage.capacity_kg,
    )


if __name__ == "__main__":
    main()
