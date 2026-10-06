"""Happy-path tests for rule-based EMS dispatch."""

import pytest


def test_surplus_dispatch_charges_supercapacitor(energy_manager):
    result = energy_manager.dispatch(
        solar_power_kw=8.0,
        load_power_kw=3.0,
        time_step_hours=1.0,
    )

    assert result["energy_status"] == "BALANCED"
    assert result["supercapacitor_charged_kwh"] == 5.0
    assert result["hydrogen_produced_kg"] == 0.0
    assert result["net_after_storage_kw"] == 0.0


def test_deficit_dispatch_uses_supercapacitor_first(energy_manager):
    result = energy_manager.dispatch(
        solar_power_kw=3.0,
        load_power_kw=8.0,
        time_step_hours=1.0,
    )

    assert result["energy_status"] == "BALANCED"
    assert result["supercapacitor_discharged_kwh"] == 5.0
    assert result["hydrogen_used_kg"] == 0.0
    assert result["net_after_storage_kw"] == 0.0


def test_deficit_dispatch_uses_hydrogen_after_supercapacitor(energy_manager):
    result = energy_manager.dispatch(
        solar_power_kw=0.0,
        load_power_kw=8.0,
        time_step_hours=1.0,
    )

    assert result["supercapacitor_discharged_kwh"] == 5.0
    assert result["hydrogen_used_kg"] == pytest.approx(3.0 / 33.33)
    assert result["net_after_storage_kw"] == pytest.approx(0.0)


def test_balanced_dispatch_does_not_change_storage(energy_manager):
    result = energy_manager.dispatch(
        solar_power_kw=4.0,
        load_power_kw=4.0,
        time_step_hours=1.0,
    )

    assert result["energy_status"] == "BALANCED"
    assert result["supercapacitor_energy_kwh"] == 5.0
    assert result["hydrogen_inventory_kg"] == 0.5
